from logging.config import dictConfig


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(levelname)s] [%(name)s] %(message)s'
        }
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'DEBUG',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'wordcounter': {
            'handlers': ['stdout'],
            'level': 'DEBUG',
            'propagate': True
        }
    },
    'root': {
        'handlers': ['stdout'],
        'level': 'DEBUG'
    }
}


dictConfig(LOGGING)
