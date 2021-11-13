from aiogram.types import Message
from aiogram.utils import executor
from aiogram.types.input_media import InputMediaPhoto
from keyboards.default.buttons import *
from config import *
from consts import dp, bot
from messager import *


@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: Message):
    await message.reply(get_msg("help"), reply_markup=greet_kb)


@dp.message_handler()
async def echo_message(msg: Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)
