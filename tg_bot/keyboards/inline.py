"""
Клавиатура списка акций
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from tg_bot.keyboards.callback_data_factory import stocks_callback

stocks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🦷Имплантация Osstem от 1200 рублей в месяц",
                callback_data=stocks_callback.new(
                    stock_name="osstem",
                    stock_date="до 30.08.2023"
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="💎Профессиональная гигиена полости рта всего за 3000 руб",
                callback_data=stocks_callback.new(
                    stock_name="hygiene",
                    stock_date="до 30.08.2023"
                ),
            )
        ],
        [
            InlineKeyboardButton(
                text="😁Брекет-система (производство США) от 1100 руб/мес",
                callback_data=stocks_callback.new(
                    stock_name="brecket",
                    stock_date="до 30.07.2023"
                ),
            )
        ],
        [InlineKeyboardButton(text="↩️На главное меню",
                              callback_data="cancel")],
    ]
)
