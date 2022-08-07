from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message

from api import session_manager

storage = MemoryStorage()
bot = Bot(token='token', parse_mode='html')
dp = Dispatcher(bot, storage=storage)
Api = session_manager.YandexTTS()


@dp.message_handler(commands=["start"])
async def start(msg: Message):
    await msg.answer('Введите любой текст, алиса озвучит его')


@dp.message_handler()
async def t_audio(msg: Message):
    x = await Api.send_tts(msg.text, format=session_manager.Formats.OGGOPUS)
    if x[0]:
        await msg.answer_audio(x)
    else:
        await msg.answer(f'<code>{x[1]}</>')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
