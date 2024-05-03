from dotenv import load_dotenv
from os import getenv


load_dotenv()
# Токен для Телеграм бота
TOKEN = getenv("TELEGRAM_TOKEN")

# путь к iam.json
TOKEN_PATH ="/home/student/Jarvis_v1/iam_token.json"
FOLDER_ID_PATH = "/home/student/Jarvis_v1/test.txt"

# Параметры для Yandex API
METADATA_URL = "http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token"

# URLs для Yandex SpeechKit
STT_URL = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"
TTS_URL = "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize"


# URLs для Yandex GPT
TOKENIZE_COMPLETION_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/tokenizeCompletion"
COMPLETION_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"


# Параметры для Yandex SpeechKit
RECOGNITION_TOPIC = "general"
LANGUAGE_CODE = "ru-RU"
TTS_VOICE = "filipp"
TTS_EMOTION = "good"
TTS_FORMAT = "oggopus"

# Параметры для Yandex GPT
MAX_GPT_TOKENS = 120
GPT_TEMPERATURE = 0.7  # Настройка температуры для модели GPT
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты супкр мозг, ты знаешь все и вся. И отвечаешь четко и кратко'}]

# Лимиты и настройки использования
MAX_USERS = 3
N_LAST_MESSAGE = 4
MAX_TIME_VOICE = 30
TIME_NOT_ACTIVE = 60

# Лимиты для пользователя
MAX_USER_STT_BLOCKS = 10
MAX_USER_TTS_SYMBOLS = 5000
MAX_USER_GPT_TOKENS = 5000


# Параметры для логирования
LOGS = 'logs_new.txt'

# Параметры базы данных
DB_FILE = 'messages_new.db'