"""
Модуль чата с администратором Middleware
"""
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types, Dispatcher, Bot
from tg_bot.config import load_config

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
dp = Dispatcher(bot)


class SupportMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, massage: types.Message, data: dict):
        state = dp.current_state(chat=massage.from_user.id,
                                 user=massage.from_user.id)
        state_str = str(await state.get_state())
        if state_str == "in_support":
            data = await state.get_data()
            second_id = data.get("second_id")

            await massage.copy_to(second_id)

            raise CancelHandler()
