import logging

from tg_bot.keyboards.callback_data_factory import stocks_callback
from tg_bot.keyboards.reply import menu
from tg_bot.keyboards.stock_keyboards import (
    osstem_keyboard,
    brecket_keyboard,
    hygiene_keyboard,
)
from tg_bot.misc.main_text import stocks_brecket, stocks_all_on_4
from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from tg_bot.models.db_commands import select_stock

"""
Функции обработки кнопок списка акций
"""


@rate_limit(2)
async def osstem_btn(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    # stock_date = stocks_callback.get("stock_date")
    stock = await select_stock(1)
    await call.message.answer_photo(
        stock.stock_image,
        caption=f"{stock.stock_name}\n" f"{stock.stock_description}",
        reply_markup=osstem_keyboard,
    )


@rate_limit(2)
async def hygiene_btn(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    # stock_date = stocks_callback.get("stock_date")
    stock = await select_stock(2)
    await call.message.answer_photo(
        stock.stock_image,
        caption=f"{stock.stock_name}\n" f"{stock.stock_description}",
        reply_markup=hygiene_keyboard,
    )


@rate_limit(2)
async def brecket_btn(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    # stock_date = stocks_callback.get("stock_date")
    stock = await select_stock(3)
    await call.message.answer_photo(
        stock.stock_image,
        caption=f"{stock.stock_name}\n" f"{stock.stock_description}",
        reply_markup=brecket_keyboard,
    )


@rate_limit(2)
async def cancel_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Главное меню: ", reply_markup=menu)


def register_stocks(dp: Dispatcher):
    dp.register_callback_query_handler(
        osstem_btn, stocks_callback.filter(stock_name="osstem")
    )
    dp.register_callback_query_handler(
        hygiene_btn, stocks_callback.filter(stock_name="hygiene")
    )
    dp.register_callback_query_handler(
        brecket_btn, stocks_callback.filter(stock_name="brecket")
    )
    dp.register_callback_query_handler(cancel_btn, Text(equals="cancel"))
