"""
Клавиатура вызова такси
"""
from aiogram.types import InlineKeyboardButton, \
    InlineKeyboardMarkup, \
    WebAppInfo

taxi_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚖Вызвать такси",
                web_app=WebAppInfo(url="https://clck.ru/35H49x")
            )
        ],
        [InlineKeyboardButton(text="↩️На главное меню",
                              callback_data="cancel")],
    ]
)
