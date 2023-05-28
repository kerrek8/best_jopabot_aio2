from loader import dp, bot
from aiogram import types
from config import foto_dubai_id


@dp.message_handler(commands=['dubai'])
async def dubai(messenge: types.Message):
    await bot.send_photo(messenge.chat.id, foto_dubai_id)
