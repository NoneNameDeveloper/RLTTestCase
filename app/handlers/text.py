from aiogram import types

from aiogram import F

from app.engine.db.service import aggregate_salary_data
from app.engine.utils import validate_request
from loader import dp


@dp.message(F.text)
async def text_handler(message: types.Message):

    # getting user input
    user_input = message.text

    # validating and getting python object (dict)
    user_input_validated: bool | dict = validate_request(user_input)

    aggregated_data = aggregate_salary_data(user_input_validated['dt_from'],
                                            user_input_validated['dt_upto'],
                                            user_input_validated['group_type'])

    await message.answer(str(aggregated_data))
