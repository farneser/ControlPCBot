from loader import bot, storage


async def on_shutdown(arg):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from modules.handlers import dp
    executor.start_polling(dp, on_shutdown=on_shutdown)
