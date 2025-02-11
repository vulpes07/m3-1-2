import asyncio
import logging
from logging import basicConfig
from bot import bot, dp
import echo, start, help


async def main():
    logging.basicConfig(level=logging.INFO)

    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(echo.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



