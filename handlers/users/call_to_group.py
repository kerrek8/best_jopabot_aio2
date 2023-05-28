from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.states import WaitToCall


@dp.message_handler(commands=['call'])
async def call(msg: types.Message):
    if msg.from_user.id == 1090101751:
        await WaitToCall.callhandlerstate.set()
        await bot.send_message(msg.chat.id, 'отправляй сообщения и я перешлю их в жопу')


@dp.message_handler(commands=['exit'], state='*')
async def escape(msg: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(msg.chat.id, 'обращайся')


@dp.message_handler(state=WaitToCall.callhandlerstate)
async def enter(msg: types.Message):
    await bot.send_message(-1001841458995, msg.text)
