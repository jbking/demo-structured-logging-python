import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'stream': 'ext://sys.stderr',
            'formatter': 'simple',
        },
        'debug_to_file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'filename': 'debug.log',
            'formatter': 'simple',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['default'],
    },
    'loggers': {
        'example.a.c': {
            'level': 'DEBUG',
            'handlers': ['debug_to_file'],
        },
    }
})

import example.a.c
import example.b
