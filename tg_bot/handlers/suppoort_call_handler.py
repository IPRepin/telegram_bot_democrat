"""
Модуль обработки связи пользователя с администратором
в режиме чата
"""
from aiogram.dispatcher import FSMContext

from tg_bot.config import load_config
from tg_bot.keyboards.suppot_keyboard import (
    support_keyboards,
    check_support_available,
    get_support_manager,
    cancel_support,
)
from tg_bot.keyboards.callback_data_factory import (
    support_callback,
    cancel_support_callback,
)
from tg_bot.misc.throttling import rate_limit
from aiogram import types, Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

config = load_config(".env")

bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())


@rate_limit(2)
async def send_to_support_call(
    call: types.CallbackQuery, state: FSMContext, callback_data: dict
):
    await call.answer()
    await call.message.answer("Отправьте сообщение администратору!")
    user_id = int(callback_data.get("user_id"))
    if not await check_support_available(user_id):
        support_id = await get_support_manager()
    else:
        support_id = user_id

    if not support_id:
        await call.message.answer("Все администраторы заняты \
        попробуйте позже!")
        await state.reset_state()
        return

    await state.set_state("wait_in_support")
    await state.update_data(second_id=support_id)

    keybord = await support_keyboards(messages="many",
                                      user_id=call.from_user.id)
    await bot.send_message(
        support_id,
        f"Вам пришло сообщение от пользователя\
         {call.from_user.full_name}",
        reply_markup=keybord,
    )


@rate_limit(2)
async def answer_support_call(
    call: types.CallbackQuery, state: FSMContext, callback_data: dict
):
    second_id = int(callback_data.get("user_id"))
    user_state = dp.current_state(user=second_id, chat=second_id)

    if str(await user_state.get_state()) != "wait_in_support":
        await call.message.edit_text("Пользователь уже покинул чат")
        return
    await state.set_state("in_support")
    await user_state.set_state("in_support")

    await state.update_data(second_id=second_id)

    keyboard = cancel_support(second_id)
    keyboard_second_user = cancel_support(call.from_user.id)

    await call.message.edit_text(
        "Чтобы завершить общение нажмите на кнопку ниже", reply_markup=keyboard
    )
    await bot.send_message(
        second_id,
        "Администратор на связи!\n" "Чтобы завершить общение нажмите на кнопку ниже",
        reply_markup=keyboard_second_user,
    )


@rate_limit(2)
async def not_supported(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get("second_id")
    keybord = await cancel_support(user_id=second_id)
    await message.answer(
        "Дождитесь ответа от оператора или отмените сеанс",
        reply_markup=keybord
    )


@rate_limit(2)
async def exit_support(
    call: types.CallbackQuery, state: FSMContext, callback_data: dict
):
    user_id = int(callback_data.get("user_id"))
    second_state = dp.current_state(user=user_id, chat=user_id)

    if await second_state.set_state() is not None:
        data_second = second_state.get_data()
        second_id = data_second.get("second_id")
        if int(second_id) == call.from_user.id:
            await second_state.reset_state()
            await bot.send_message(user_id, "Пользователь завершил сеанс")

    await call.message.edit_text("Сеанс завершен")
    await state.reset_state()


def register_support_coll(dp: Dispatcher):
    dp.register_callback_query_handler(
        send_to_support_call, support_callback.filter(messages="many",
                                                      as_user="yes")
    )
    dp.register_callback_query_handler(
        answer_support_call, support_callback.filter(messages="many",
                                                     as_user="no")
    )
    dp.register_message_handler(
        not_supported, state="wait_in_support",
        content_types=types.ContentTypes.ANY
    )
    dp.register_callback_query_handler(
        exit_support,
        cancel_support_callback.filter(),
        state=["in_support", "wait_in_support", None],
    )
