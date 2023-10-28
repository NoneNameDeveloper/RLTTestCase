from aiogram import Bot, Dispatcher

from app.data import Config


bot = Bot(token=Config.BOT_TOKEN)

dp = Dispatcher()
