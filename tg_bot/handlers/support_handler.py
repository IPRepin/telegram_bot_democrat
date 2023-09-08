"""
Модуль обработки связи пользователя с администратором
в режиме вопрос-ответ
"""

from aiogram.dispatcher import FSMContext

from tg_bot.config import load_config
from tg_bot.keyboards.suppot_keyboard import support_keyboards
from tg_bot.keyboards.callback_data_factory import support_callback
from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher, Bot

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode="HTML")


@rate_limit(2)
async def send_to_support(
    call: types.CallbackQuery, state: FSMContext, callback_data: dict
):
    await call.answer()
    user_id = int(callback_data.get("user_id"))
    await call.message.answer("Отправьте сообщение")
    await state.set_state("wait_for_support_message")
    await state.update_data(second_id=user_id)


@rate_limit(2)
async def get_support_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data["second_id"]
    await bot.send_message(
        second_id, f"Вам пришло сообщение, чтобы ответить \
        нажмите на кнопку ниже⬇️"
    )
    keyword = await support_keyboards(messages="one",
                                      user_id=message.from_user.id)
    await message.copy_to(second_id,
                          reply_markup=keyword)
    await message.answer("Сообщение отправлено")
    await state.reset_state()


def register_support(dp: Dispatcher):
    dp.register_callback_query_handler(
        send_to_support, support_callback.filter(messages="one")
    )
    dp.register_message_handler(
        get_support_message,
        state="wait_for_support_message",
        content_types=types.ContentTypes.ANY,
    )
