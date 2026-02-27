import sys
from log_filters import ErrorLogFilter, CriticalLogFilter, DebugWarningLogFilter

formatters = {
    "default": {
        "format": "#%(levelname)-8s %(name)s:%(funcName)s - %(message)s -- this is root"
    },
    "formatter_1": {
        "format": "[%(asctime)s] #%(levelname)-8s %(filename)s:"
        "%(lineno)d - %(name)s:%(funcName)s - %(message)s -- this is error.log"
    },
    "formatter_2": {
        "format": "#%(levelname)-8s [%(asctime)s] - %(filename)s:"
        "%(lineno)d - %(name)s:%(funcName)s - %(message)s"
    },
    "formatter_3": {"format": "#%(levelname)-8s [%(asctime)s] - %(message)s"},
    "formatter_4": {
        "format": "#%(levelname)-8s [%(asctime)s] - %(message)s -- this is stderr"
    },
}
filters = {
    "critical_filter": {
        "()": CriticalLogFilter,
    },
    "error_filter": {
        "()": ErrorLogFilter,
    },
    "debug_warning_filter": {
        "()": DebugWarningLogFilter,
    },
}
handlers = {
    "default": {"class": "logging.StreamHandler", "formatter": "default"},
    "stderr": {
        "class": "logging.StreamHandler",
        "formatter": "formatter_4",
        "stream": sys.stderr,
    },
    "stdout": {
        "class": "logging.StreamHandler",
        "formatter": "formatter_2",
        "filters": ["debug_warning_filter"],
        "stream": sys.stdout,
    },
    "error_file": {
        "class": "logging.FileHandler",
        "filename": "error.log",
        "mode": "w",
        "level": "DEBUG",
        "formatter": "formatter_1",
        "filters": ["error_filter"],
    },
    "critical_file": {
        "class": "logging.FileHandler",
        "filename": "critical.log",
        "mode": "w",
        "formatter": "formatter_3",
        "filters": ["critical_filter"],
    },
}
loggers = {
    "telegram_bot.m_1": {"level": "DEBUG", "handlers": ["stderr", "error_file"]},
    "telegram_bot.m_2": {"level": "DEBUG", "handlers": ["critical_file"]},
}
root = {"formatter": "default", "handlers": ["default"]}


logging_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": formatters,
    "filters": filters,
    "handlers": handlers,
    "loggers": loggers,
    "root": root,
}
