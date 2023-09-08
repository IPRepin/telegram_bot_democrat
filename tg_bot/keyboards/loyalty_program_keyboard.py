"""
Клавиатура программы лояльности (не используется)
"""
from aiogram.types import InlineKeyboardButton, \
    InlineKeyboardMarkup


admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📲Связаться через телеграм",
                url="https://t.me/+79302077377"
            )
        ],
        [InlineKeyboardButton(text="↩️На главное меню",
                              callback_data="cancel")],
    ]
)
