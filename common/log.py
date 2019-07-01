# -*- coding:utf-8 -*-
import logging.config
import os

from webchat.settings import BASE_DIR

LOG_DICT = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[%(asctime)s]: %(filename)s--line:%(lineno)d[%(levelname)s]:%(message)s"
        },
        "verbose": {
            "format": "[%(asctime)s]: %(filename)s--%(funcName)s--line:%(lineno)d [%(levelname)s]:%(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "verbose",
            "stream": "ext://sys.stdout"
        },
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "verbose",
            "filename": os.path.join(BASE_DIR, 'logs', 'info.log'),
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "verbose",
            "filename": os.path.join(BASE_DIR, 'logs', 'error.log'),
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },
    "loggers": {
        "main": {
            "level": "INFO",
            "handlers": ["info_file_handler", "error_file_handler", "console"],
            "propagate": "no"
        }
    },
    # "root": {
    #     "level": "ERROR",
    #     "handlers": ["console", "info_file_handler", "error_file_handler"]
    # }
}
log_path = os.path.join(BASE_DIR, 'logs')
if not os.path.isdir(log_path):
    os.mkdir(log_path)
logging.config.dictConfig(LOG_DICT)

logger = logging.getLogger('main')

