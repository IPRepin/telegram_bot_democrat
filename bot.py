"""
Модуль запуска бота
"""

import asyncio
import logging

import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "democrat_admin.democrat_admin.settings"
)
os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE": "true"})
django.setup()

from tg_bot.handlers.admin import register_admin
from tg_bot.handlers.handler_states_recording import register_states_recording
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher.middlewares import BaseMiddleware

from tg_bot.config import load_config
from tg_bot.filters.admin import AdminFilter
from tg_bot.handlers.channel_handler import register_channel_handler
from tg_bot.handlers.entries_handler import register_entries
from tg_bot.handlers.recording_handler import register_recording
from tg_bot.handlers.stocks_handler import register_stocks
from tg_bot.handlers.suppoort_call_handler import register_support_coll
from tg_bot.handlers.support_handler import register_support
from tg_bot.handlers.user import register_user
from tg_bot.middleware.support_middleware import SupportMiddleware
from tg_bot.middleware.thottling import ThrottlingMiddleware
from tg_bot.filters.censorship import register_censorship
from tg_bot.misc.set_bot_commands import set_default_commands

logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    dp.setup_middleware(ThrottlingMiddleware(BaseMiddleware))
    dp.setup_middleware(SupportMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_admin(dp)
    register_user(dp)
    register_support(dp)
    register_support_coll(dp)
    register_stocks(dp)
    register_entries(dp)
    register_states_recording(dp)
    register_recording(dp)
    register_channel_handler(dp)
    register_censorship(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )

    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    bot["config"] = config

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await set_default_commands(bot)
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот остановлен!")
