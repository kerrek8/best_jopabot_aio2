from loader import dp, bot
from aiogram import types
import os
import sys



@dp.message_handler(commands=['restart'])
async def restart(message: types.Message):
    await bot.send_message(message.from_user.id, 'Restarting...')
    # os.execl(sys.executable, sys.executable, *sys.argv)
