from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

from api import session_manager

storage = MemoryStorage()
bot = Bot(token='5152791752:AAEEzx6yVn2V7JdAV-GpLVcE5VEaCewATb8', parse_mode='html')
dp = Dispatcher(bot, storage=storage)
Api = session_manager.YandexTTS()


@dp.message_handler(commands=["start"])
async def start(msg: Message):
    await msg.answer('Введите любой текст, алиса озвучит его')


def re_speech(text: str) -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text='🔄 Повторить', callback_data=f'respeech|{text}')
        ]
    ])


@dp.message_handler()
async def t_audio(msg: Message):
    x = await Api.send_tts(msg.text, format=session_manager.Formats.MP3)
    if x[0]:
        await msg.answer_audio(x, reply_markup=re_speech(msg.text))
    else:
        await msg.answer(f'<code>{x[1]}</>')


@dp.callback_query_handler(text_startswith='respeech|')
async def respeech_call(call: types.CallbackQuery):
    text = call.data.split('|')[1]
    x = await Api.send_tts(text)
    await call.message.edit_media()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
