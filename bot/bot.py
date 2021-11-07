from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from  aiogram.types.input_media import *
from keyboards.default.buttons import *


from config import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['group'])
async def process_group_command(message: types.Message):
    media = [InputMediaPhoto("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2019-honda-civic-sedan-1558453497.jpg")]
    for photo_id in range(2):
        media.append(InputMediaPhoto("https://auto1-homepage.prod.mp.auto1.cloud/static/optimized/orange-car-hp-right-mercedez.png"))
    await bot.send_media_group(message.from_user.id, media)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!", reply_markup=greet_kb)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)