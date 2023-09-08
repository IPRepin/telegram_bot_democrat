"""
Модуль подключения к АМО CRM
"""

from amocrm.v2 import tokens


def connect_amo():
    tokens.default_token_manager(
        client_id="<ID из вкладки 'Ключи и доступы' созданной вами интеграции>",
        client_secret="<Секретный ключ из вкладки Ключи и доступы созданной вами интеграции>",
        subdomain="<Субдомен вашей организации в АМО CRM>",
        redirect_url="<Сайт вашей организации>",
        storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
    )

    tokens.default_token_manager.init(code="<Код авторизации из вкладки Ключи и доступы созданной вами интеграции>",
                                      skip_error=False)
