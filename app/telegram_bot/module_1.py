import logging

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)
print(__name__)
logger.propagate = True

# Устанавливаем логгеру уровень `DEBUG`
logger.setLevel(logging.DEBUG)


# Определяем свой фильтр, наследуясь от класса Filter библиотеки logging
class ErrorLogFilter(logging.Filter):
    # Переопределяем метод filter, который принимает `self` и `record`
    # Переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, record: logging.LogRecord):
        return record.levelname == "ERROR"


# Инициализируем форматтер
formatter_1 = logging.Formatter(
    fmt="[%(asctime)s] #%(levelname)-8s %(filename)s:"
    "%(lineno)d - %(name)s:%(funcName)s - %(message)s -- this is error.log"
)
formatter_11 = logging.Formatter(
    fmt="#%(levelname)-8s [%(asctime)s] - %(message)s -- this is stderr"
)

# Инициализируем хэндлер, который будет писать логи в файл `error.log`
error_file_handler = logging.FileHandler("error.log", "w", "utf-8")
# Устанавливаем хэндлеру уровень `DEBUG`
error_file_handler.setLevel(logging.DEBUG)

# Добавляем хэндлеру фильтр `ErrorLogFilter`, который будет пропускать в
# хэндлер только логи уровня `ERROR`
error_file_handler.addFilter(ErrorLogFilter())
stderr_handler = logging.StreamHandler()
# Определяем форматирование логов в хэндлере
error_file_handler.setFormatter(formatter_1)
stderr_handler.setFormatter(formatter_11)

# Добавляем хэндлер в логгер
logger.addHandler(error_file_handler)
logger.addHandler(stderr_handler)


def func_1():
    print("This is func_1")
    logger.debug("Лог DEBUG")
    logger.info("Лог INFO")
    logger.warning("Лог WARNING")
    logger.error("Лог ERROR")
    logger.critical("Лог CRITICAL")
