"""
Модуль машины состояний получения данных пользователя
и их передачи в АМО.
"""

from aiogram.dispatcher import FSMContext

from api_amo.amo_commands import add_contact
from tg_bot.keyboards.reply import menu
from tg_bot.misc.main_text import waiting_text
from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from tg_bot.misc.states_online_recording import OnlineRecording
from tg_bot.models import db_commands as commands

import asyncio

"""
Функция получения имени
пользователя в АМО
"""


@rate_limit(2)
async def enter_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Введите имя:")
    await OnlineRecording.NAME.set()
    await asyncio.sleep(40)
    if await state.get_state() == "OnlineRecording:NAME":
        await call.message.answer(waiting_text, reply_markup=menu)
        await state.finish()
        

"""
Функция получения номера телефона
пользователя в АМО
"""


@rate_limit(2)
async def enter_phone(message: types.Message, state: FSMContext):
    await state.update_data(answer_name=message.text)
    await message.answer("Введите номер телефона:")
    await OnlineRecording.PHONE.set()
    await asyncio.sleep(40)
    if await state.get_state() == "OnlineRecording:PHONE":
        await message.answer(waiting_text, reply_markup=menu)
        await state.finish()


"""
Функция получения передачи данных
пользователя в АМО
"""


@rate_limit(2)
async def end_enter(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("answer_name")
    phone = message.text
    await message.answer(
        f"Спасибо {name} ваш номер {phone}\n"
        f"Администратор свяжется с вами в течении 10 минут.",
        reply_markup=menu,
    )
    await commands.add_patient(user_id=message.from_user.id, name=name, phone=phone)
    await add_contact(name=name, phone=phone)
    await state.finish()


def register_states_recording(dp: Dispatcher):
    dp.register_callback_query_handler(enter_name, Text(equals="rec_online"), state=None)
    dp.register_message_handler(enter_phone, state=OnlineRecording.NAME)
    dp.register_message_handler(end_enter, state=OnlineRecording.PHONE)
