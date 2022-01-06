from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_help = InlineKeyboardButton('О боте', callback_data='button1')
inline_help_kb = InlineKeyboardMarkup().add(inline_help)
