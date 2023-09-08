from tg_bot.keyboards.add_entries_keyboard import add_number
from tg_bot.keyboards.reply import menu
from tg_bot.misc.main_text import text_admin_entries
from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

"""
Функции обработки кнопок онлайн записи
"""


@rate_limit(2)
async def recording_btn(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(text_admin_entries, reply_markup=add_number)


@rate_limit(2)
async def go_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=menu)


@rate_limit(2)
async def get_contact(message: types.Message):
    contact = message.contact
    await message.answer(
        f"Спасибо {contact.full_name}\n"
        f"Администратор свяжется с вами в течении 10 минут.",
        reply_markup=menu,
    )


def register_recording(dp: Dispatcher):
    dp.register_callback_query_handler(recording_btn,
                                       Text(equals="admin_btn"))
    dp.register_message_handler(go_main_menu,
                                Text(endswith="главное меню"))
    dp.register_message_handler(get_contact,
                                content_types=types.ContentType.CONTACT)
