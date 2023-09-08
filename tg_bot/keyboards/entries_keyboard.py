"""
Клавиатуры для онлайн записи при отсутствии активных записей в АМО
"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

not_entries_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌐Онлайн запись",
                              callback_data="rec_online")],
        [InlineKeyboardButton(text="↩️На главное меню",
                              callback_data="cancel")],
    ]
)

# list_of_entries_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#
#     ]
# )
