import json
import os
import time
from datetime import datetime, timedelta
import requests
import logging

from config import TOKEN_PATH, FOLDER_ID_PATH, METADATA_URL

# Настройка логирования с указанием уровня, файла, режима записи и формата сообщений.
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

def create_new_token():
    """Создание нового токена"""
    headers = {"Metadata-Flavor": "Google"}  # Заголовки для запроса к метаданным Google.

    token_dir = os.path.dirname(TOKEN_PATH)  # Получение директории файла токена.
    if not os.path.exists(token_dir):  # Проверка наличия директории.
        os.makedirs(token_dir)  # Создание директории, если она не существует.
        logging.info(f"Directory created: {token_dir}")  # Логирование создания директории.

    try:
        logging.info("Attempting to retrieve the token...")  # Логирование попытки получения токена.
        response = requests.get(METADATA_URL, headers=headers)  # Отправка запроса на получение токена.
        if response.status_code == 200:  # Проверка статуса ответа.
            token_data = response.json()  # Разбор тела ответа как JSON.
            logging.info("Token retrieved successfully.")  # Логирование успешного получения токена.

            # Вычисление времени истечения токена и добавление его в данные токена.
            expires_at = datetime.now() + timedelta(seconds=token_data['expires_in'])
            token_data['expires_at'] = expires_at.isoformat()

            with open(TOKEN_PATH, "w") as token_file:  # Открытие файла для записи.
                json.dump(token_data, token_file)  # Запись данных токена в файл.
                logging.info(f"Token written to file: {TOKEN_PATH}")  # Логирование записи токена в файл.

        else:
            logging.error(f"Failed to retrieve token. Status code: {response.status_code}")  # Логирование ошибки получения токена.
    except Exception as e:
        logging.error(f"An error occurred while retrieving token: {str(e)}")  # Логирование возникновения исключения.

def get_creds() -> (str, str):
    """Получение токена и folder_id из yandex cloud command line interface"""
    try:
        with open(TOKEN_PATH, 'r') as f:  # Открытие файла токена для чтения.
            d = json.load(f)  # Загрузка данных из файла.
            expiration = datetime.fromisoformat(d["expires_at"])  # Преобразование строки времени истечения в объект datetime.

        if expiration < datetime.now():  # Проверка, не истек ли токен.
            logging.info("Token expired. Creating new token...")  # Логирование истечения срока действия токена.
            create_new_token()  # Создание нового токена.
            with open(TOKEN_PATH, 'r') as f:  # Повторное открытие файла токена для чтения.
                d = json.load(f)  # Повторная загрузка данных.

    except Exception as e:
        logging.error(f"Error reading token file: {str(e)}")  # Логирование ошибки чтения файла.
        create_new_token()  # Создание нового токена при возникновении ошибки.
        with open(TOKEN_PATH, 'r') as f:  # Повторное открытие файла.
            d = json.load(f)  # Повторная загрузка данных.

    token = d["access_token"]  # Получение значения токена.

    with open(FOLDER_ID_PATH, 'r') as f:  # Открытие файла для чтения ID папки.
        folder_id = f.read().strip()  # Чтение и удаление пробельных символов.

    return token, folder_id  # Возврат токена и ID папки.
