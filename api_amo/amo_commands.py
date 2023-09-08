"""
Модуль команд работы с AMO CRM
"""

from amocrm.v2 import Lead as _Lead, custom_field
from api_amo.connect_api_amo import connect_amo
from asgiref.sync import sync_to_async
from datetime import datetime

from tg_bot.misc.main_text import text_story_recording

"""
Класс определения полей с данными АМО
"""


class Lead(_Lead):
    Source_phone = custom_field.TextCustomField("Source_phone")
    rec_date = custom_field.TextCustomField("Дата записи")
    rec_time = custom_field.TextCustomField("Время записи")
    doctor = custom_field.TextCustomField("ФИО врача")


"""
Функция добавления записи пользователя в АМО
"""


@sync_to_async()
def add_contact(name: str, phone: str):
    name = f"Телеграмм {name} {phone}"
    connect_amo()
    create_contact = Lead.objects.create(name=name)
    create_contact.Source_phone = phone
    create_contact.save()


"""
Функция извлечения информации о записи пользователя из АМО
"""


def info(phone):
    connect_amo()
    try:
        lead = Lead.objects.get(query=phone)
        date = datetime.fromtimestamp(lead.rec_date).strftime("%d.%m.%Y")
        time = lead.rec_time
        doctor = lead.doctor
        return f"Вы записаны {date} на {time} к доктору {doctor}"
    except Exception:
        return text_story_recording
