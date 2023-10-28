from aiogram import types

from aiogram.filters import CommandStart

from loader import dp


@dp.message(CommandStart())
async def start_handler(message: types.Message):

    await message.answer(f"Hi, {message.from_user.full_name}!")