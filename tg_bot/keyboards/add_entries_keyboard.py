"""
Клавиатура записи пользователя
"""

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)


online_entries_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌐Онлайн запись", callback_data="rec_online")],
        [
            InlineKeyboardButton(
                text="📲Связаться через телеграм",
                # callback_data='admin_btn',
                url="https://t.me/+79302077377",
            )
        ],
        [InlineKeyboardButton(text="↩️На главное меню", callback_data="cancel")],
    ]
)

add_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱Поделится номером", request_contact=True)],
        [
            KeyboardButton(
                text="↩️На главное меню",
            )
        ],
    ],
    resize_keyboard=True,
)
