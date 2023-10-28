import asyncio
import sys

from loader import bot, dp

from app import handlers

from app.engine.db.db import init_db

import logging


async def main():
    """tasks started on app startup"""
    init_db()  # mongodb db initializing

    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    asyncio.run(main())

