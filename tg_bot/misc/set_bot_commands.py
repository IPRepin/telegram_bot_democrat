"""
Модуль дефолтных команд бота
"""
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="start",
                   description="Запустить бота"),
        BotCommand(command="help",
                   description="Что умеет этот бот"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def set_default_admin_commands(bot: Bot):
    commands = [
        BotCommand(command="newsletter",
                   description="Отправить последнюю рассылку"),
        BotCommand(command="help",
                   description="Что умеет этот бот"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
