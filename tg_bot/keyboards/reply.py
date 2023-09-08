from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="💫Акции и скидки"),
        ],
        [
            KeyboardButton(text="📑Ваши записи"),
            KeyboardButton(text="✅Записаться на прием"),
        ],
        [KeyboardButton(text="🚕Такси до клиники")],
        [KeyboardButton(text="🤩Скидка 5️% за отзыв о клинике")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
