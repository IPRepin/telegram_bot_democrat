"""
Модуль эхо бот (не используется)
"""
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.markdown import hcode
from tg_bot.misc.throttling import rate_limit
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@rate_limit(2)
async def bot_echo(message: types.Message):
    text = ["Эхо без состояния", "Сообщение:", message.text]
    await message.answer(
        "\n".join(text),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Button", callback_data="button")]
            ]
        ),
    )


@rate_limit(2)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    message.get_args()
    text = [f"Эхо в состоянии {hcode(state_name)}", "Сообщение:", message.text]
    await message.answer("\n".join(text))


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(
        bot_echo_all, state="*", content_types=types.ContentType.ANY
    )
