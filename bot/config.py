from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 16930870))
    API_HASH = env.get("TELEGRAM_API_HASH", "97c229adccadb2fc1e81b4f1ce8b22e9")
    OWNER_ID = int(env.get("OWNER_ID", 5829124764))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "bdzfilestreambot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6559235534:AAGjZ759ohs6V_OK__aLkNjzIsdIOqrtYZ4")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002064786619))
    BOT_WORKERS = int(env.get("BOT_WORKERS", 15))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 9))

class Server:
    BASE_URL = env.get("BASE_URL", "http://127.0.0.1:8080")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
