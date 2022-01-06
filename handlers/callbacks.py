from aiogram import types
from creations import dp, bot

async def proccess_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Это тестовый бот для обучения и практики!")

def register_callbacks():
    dp.register_callback_query_handler(proccess_callback_button1 ,lambda c: c.data == 'button1')
