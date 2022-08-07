import os
from typing import Union, Tuple

import pyglet
from aiohttp import ClientSession
from .random_manager import Randomus

from pydub import AudioSegment
from pydub.playback import play


class Languages:
    ru = 'ru-RU'
    en = 'en-US'
    tr = 'tr-TR'


class Voices:
    Alena = 'alena'
    Philipp = 'philipp'
    Alyss = 'alyss'
    Jane = 'jane'
    Omazh = 'omazh'
    Zahar = 'zahar'
    Ermil = 'ermil'


class Emotions:
    Neutral = 'neutral'
    Good = 'good'


class Formats:
    LPCM = 'lpcm'
    OGGOPUS = 'oggopus'
    MP3 = 'mp3'


class YandexTTS:
    def __init__(self):
        self.session = ClientSession

    async def send_tts(self,
                       message: str,
                       language: Languages = Languages.ru,
                       speed: float = 1.0,
                       voice: [Voices, str] = Voices.Alena,
                       emotion: [Emotions, str] = Emotions.Neutral,
                       format: [Formats, str] = Formats.OGGOPUS,
                       **kwargs
                       ) -> Union[bytes, tuple[bool, str]]:
        session = self.session()

        json_data = {
            'message': message,
            'language': language,
            'speed': speed,
            'voice': voice,
            'emotion': emotion,
            'format': format,
        }

        response = await session.post('https://cloud.yandex.ru/api/speechkit/tts', cookies=Randomus.cookies,
                                      headers=Randomus.headers, json=json_data)

        if response.ok:
            content = await response.content.read()

            response.close()
            await session.close()

            return content
        else:

            text = await response.json()
            response.close()
            await session.close()

            return False, text

    def play_tts(self, audio: bytes):
        # import required modules
        import subprocess, os

        open('audio.mp3', 'wb').write(audio)

        subprocess.call(["ffplay", "-nodisp", "-autoexit", 'audio.mp3'])
        # os.remove('audio.mp3')

    def _Inv(self, **kwargs):
        import speech_recognition as sr

        open('audio.mp3', 'wb').write(kwargs['data'])

        file = sr.AudioFile('audio.mp3')
        r = sr.Recognizer()

        with file as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            result = r.recognize_google(audio, language='ru')
            print(result)

