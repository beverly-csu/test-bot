from aiogram import Bot, Dispatcher, types, executor
import logging
from configparser import ConfigParser

TOKEN = "5399536895:AAFn9xNHL_qf0WSfnAQ-_9HB3WeeHwgm4HE"

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("WORK!")


executor.start_polling(dp, skip_updates=True)
