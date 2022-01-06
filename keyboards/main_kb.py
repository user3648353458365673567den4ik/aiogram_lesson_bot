from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_help = KeyboardButton('/help')
button_random = KeyboardButton('/random')
button_myinfo = KeyboardButton('/myinfo')
button_joke = KeyboardButton('/joke')

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(button_help)
main_kb.add(button_random)
main_kb.add(button_myinfo)
main_kb.add(button_joke)
