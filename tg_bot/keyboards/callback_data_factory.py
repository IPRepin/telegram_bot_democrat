"""
Модуль Callback фабрики
"""
from aiogram.utils.callback_data import CallbackData

stocks_callback = CallbackData("stock",
                               "stock_name",
                               "stock_date")
support_callback = CallbackData("ask_support",
                                "messages",
                                "user_id",
                                "as_user")
cancel_support_callback = CallbackData("cancel_support",
                                       "user_id")
