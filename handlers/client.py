from creations import dp, bot
from aiogram import types
import random

from keyboards.main_kb import main_kb
from keyboards.inline_help_kb import inline_help_kb


jokes = ["Казахам снизили цену на газ, обещают снизить цену на бензин. В России это невозможно - слишком мало казахов.",
"Вчера помог поскользнувшейся бабушке встать, а теперь ещё сегодня. Когда я загадывал поднять бабок в новом году, я имел в виду немного другое.",
"Кто сможет с похмела объяснит, почему в Советском Союзе выход на пенсию называли заслуженным отдыхом, а в путинской России - периодом дожития?",
"Мальчик, который получил на Новый год не совсем то, что хотел, сказал со стула не совсем то, что учил.",
"Антиквар решил нанять помощника и дал объявле­ние в газете. Пришёл нани­маться молодой человек. Ан­тиквар поднял с пола щеп­ку, положил её на кусок красного бархата и спросил:\n- Что это?\n- Зубочистка маркизы Помпадур.\n- Верно, - кивнул антиквар.\n - Завтра с утра вы­ходите на работу."]

# @dp.message_handler(commands=['help'])
async def proccess_help_command(message: types.Message):
    await message.reply("Привет!\nЯ учебный бот!\nВот мои команды: /help, /joke, /random, /myinfo", reply_markup=inline_help_kb)

# @dp.message_handler(commands=['joke'])
async def proccess_joke_command(message: types.Message):
    await message.reply(jokes[random.randint(0, len(jokes)-1)])

# @dp.message_handler(commands=['random'])
async def proccess_random_command(message: types.Message):
    await message.reply("Случайное число: " + str(random.randint(1,100)))

# @dp.message_handler(commands=['start'])
async def proccess_start_command(message: types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}!\nНапиши /help чтобы узнать подробности!", reply_markup=main_kb)

async def proccess_myinfo_command(message: types.Message):
    await bot.send_message(message.chat.id, f"Ваше имя и фамилия: {message.from_user.full_name}\nВаш никнейм: {message.from_user.mention}\nВаш ID Telegram: {message.from_user.id}\nВаш язык: {message.from_user.language_code.upper()}")

def register_client_handlers():
    dp.register_message_handler(proccess_help_command, commands=['help'])
    dp.register_message_handler(proccess_joke_command, commands=['joke'])
    dp.register_message_handler(proccess_random_command, commands=['random'])
    dp.register_message_handler(proccess_start_command, commands=['start'])
    dp.register_message_handler(proccess_myinfo_command, commands=['myinfo'])
