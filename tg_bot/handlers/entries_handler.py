from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

"""
Функции обработки кнопок списка записи
"""


@rate_limit(2)
async def entries_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Приложение онлайн записи")


def register_entries(dp: Dispatcher):
    dp.register_callback_query_handler(entries_btn, Text(equals="online_btn"))
