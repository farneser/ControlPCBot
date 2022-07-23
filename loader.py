import datetime
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *

try:
    bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    print(f"STARTED IN {datetime.datetime.now()}")

except Exception as _ex:
    exit(f"Error: {_ex}")
