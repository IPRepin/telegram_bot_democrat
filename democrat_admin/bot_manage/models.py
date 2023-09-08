from django.db import models

"""
Класс модели обязательных колонок создания и изменения записи
"""


class TimeBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Добавлено")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Изменено")


"""
Класс модели пользователей
"""


class User(TimeBaseModel):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(
        unique=True, default=1,
        verbose_name="ID пользователя телеграм"
    )
    name = models.CharField(max_length=250,
                            verbose_name="Имя пользователя",
                            null=True)
    user_name = models.CharField(max_length=150,
                                 verbose_name="Username телеграм")
    user_email = models.CharField(max_length=100,
                                  verbose_name="Email",
                                  null=True)
    user_url = models.TextField(max_length=200,
                                verbose_name="URL user",
                                null=True)


"""
Класс модели пациентов
"""


class Patients(TimeBaseModel):
    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(
        unique=True, default=1, verbose_name="ID пользователя телеграм"
    )
    name = models.CharField(max_length=100, verbose_name="Имя пациента")
    phone = models.TextField(max_length=12, verbose_name="Телефон пациента")


"""
Класс модели текущих акций
"""


class CurrentStocks(TimeBaseModel):
    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Текущие акции"

    id = models.AutoField(primary_key=True)
    stock_name = models.CharField(max_length=250,
                                  verbose_name="Заголовок акции")
    stock_description = models.TextField(max_length=500,
                                         verbose_name="Описание акции")
    stock_image = models.TextField(max_length=250,
                                   verbose_name="ID изображения акции")


"""
Класс модели рассылки
"""


class Mailing(TimeBaseModel):
    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    id = models.AutoField(primary_key=True)
    mailing_name = models.CharField(max_length=250,
                                    verbose_name="Заголовок рассылки")
    mailing_description = models.TextField(
        max_length=500, verbose_name="Описание рассылки"
    )
    mailing_image = models.TextField(
        max_length=250,
        verbose_name="ID изображения рассылки"
    )
    date_of_publication = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата рассылки"
    )


"""
Класс модели рефералов
"""


class Referral(TimeBaseModel):
    class Meta:
        verbose_name = "Реферал"
        verbose_name_plural = "Рефералы"

    id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    referrer_id = models.BigIntegerField()
