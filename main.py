from aiogram import types
from aiogram.utils import executor
from creations import dp

from handlers.client import register_client_handlers
from handlers.callbacks import register_callbacks


if __name__ == "__main__":
    register_client_handlers()
    register_callbacks()
    executor.start_polling(dp)
