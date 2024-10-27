import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.handlers import router
from config import TELEGRAM_TOKEN
from database.models import async_main


async def main():
    await async_main()  # create tables in the database
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
      asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")