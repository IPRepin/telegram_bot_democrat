"""
Модуль обработки входа администратора
"""
import asyncio

from aiogram import types, Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

from tg_bot.config import load_config
from tg_bot.keyboards.send_mailing_keyboard import mailing_keyboard
from tg_bot.models.db_commands import (
    select_all_users,
    select_last_mailings,
)
from tg_bot.misc.throttling import rate_limit

config = load_config(".env")

bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())


@rate_limit(2)
async def admin_start(message: types.Message):
    await message.reply("Привет админ!", reply_markup=mailing_keyboard)


@rate_limit(2)
async def send_a_newsletter(call: types.CallbackQuery):
    mailing = await select_last_mailings()
    users = await select_all_users()
    count = 0
    for user in users:
        try:
            await bot.send_photo(
                chat_id=user.user_id,
                photo=mailing.mailing_image,
                caption=f"{mailing.mailing_name}\n" 
                        f"{mailing.mailing_description}",
            )
            await asyncio.sleep(0.3)
            count += 1
        except Exception as ex:
            print(ex)
    await call.message.answer(f"Отправлено {count} сообщений")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], is_admin=True)
    dp.register_callback_query_handler(
        send_a_newsletter, Text(equals="send_mailing"), is_admin=True
    )
