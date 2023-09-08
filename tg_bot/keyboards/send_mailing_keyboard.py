"""
Клавиатуры для администратора
"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

""" Клавиатуры для отправки последней рассылки"""
mailing_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💬Отправить последнюю рассылку",
                callback_data="send_mailing"
            )
        ],
    ]
)
