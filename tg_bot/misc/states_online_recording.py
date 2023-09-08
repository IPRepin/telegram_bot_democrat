"""
Модуль определения состояний для машины состояний онлайн записи
"""
from aiogram.dispatcher.filters.state import StatesGroup, State


class OnlineRecording(StatesGroup):
    NAME = State()
    PHONE = State()
