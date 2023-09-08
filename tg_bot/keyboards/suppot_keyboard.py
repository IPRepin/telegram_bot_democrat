"""
Клавиатура связи пользователя с администратором (не используется)

"""
import random

from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, \
    InlineKeyboardButton
from tg_bot.keyboards.callback_data_factory import (
    support_callback,
    cancel_support_callback,
)
from tg_bot.config import load_config

config = load_config(".env")

dp = Dispatcher(Bot(token=config.tg_bot.token, parse_mode="HTML"))


async def check_support_available(support_id):
    state = dp.current_state(chat=support_id, user=support_id)
    state_str = str(await state.get_state())
    if state_str == "in_support":
        return
    else:
        return support_id


async def get_support_manager():
    support_ids = config.tg_bot.support_id
    random.shuffle(support_ids)
    for support_id in support_ids:
        support_id = await check_support_available(support_id)
        if support_id:
            return support_id
        else:
            return


async def support_keyboards(messages, user_id=None):
    support_ids = config.tg_bot.support_id
    if user_id:
        contact_id = user_id
        as_user = "no"
        text = "📩Ответить пользователю"
    else:
        contact_id = await get_support_manager()
        as_user = "yes"
        if messages == "many" and contact_id is None:
            return False
        elif messages == "one" and contact_id is None:
            contact_id = random.choice(support_ids)
        if messages == "one":
            text = "💬Отправить сообщение администратору"
        else:
            text = "👩🏻‍⚕Начать чат с адмиинистратором"

    support_chat_keyboard = InlineKeyboardMarkup()
    support_chat_keyboard.add(
        InlineKeyboardButton(
            text=text,
            callback_data=support_callback.new(
                messages=messages, user_id=contact_id, as_user=as_user
            ),
        )
    )
    if messages == "many":
        support_chat_keyboard.add(
            InlineKeyboardButton(
                text="Завершить чат",
                callback_data=cancel_support_callback.new(user_id=contact_id),
            )
        )

    return support_chat_keyboard


async def cancel_support(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Завершить общение",
                    callback_data=cancel_support_callback.new(user_id=user_id),
                )
            ]
        ]
    )
