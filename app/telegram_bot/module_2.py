import logging

logger = logging.getLogger(__name__)
logger.propagate = True

logger.setLevel(logging.DEBUG)


# Определяем свой фильтр, наследуясь от класса Filter библиотеки logging
class CriticalLogFilter(logging.Filter):
    # Переопределяем метод filter, который принимает `self` и `record`
    # Переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, record: logging.LogRecord):
        return record.levelname == "CRITICAL"


# Инициализируем форматтер
formatter_2 = logging.Formatter(
    fmt="#%(levelname)-8s [%(asctime)s] - %(filename)s:"
    "%(lineno)d - %(name)s:%(funcName)s - %(message)s"
)

# Инициализируем хэндлер, который будет писать логи в файл `error.log`
critical_file_handler = logging.FileHandler("critical.log", "w", "utf-8")
# Устанавливаем хэндлеру уровень `DEBUG`
critical_file_handler.setLevel(logging.DEBUG)

# Добавляем хэндлеру фильтр `ErrorLogFilter`, который будет пропускать в
# хэндлер только логи уровня `ERROR`
critical_file_handler.addFilter(CriticalLogFilter())

# Определяем форматирование логов в хэндлере
critical_file_handler.setFormatter(formatter_2)

# Добавляем хэндлер в логгер
logger.addHandler(critical_file_handler)


def func_2():
    print("This is func_2")
    logger.debug("Лог DEBUG")
    logger.info("Лог INFO")
    logger.warning("Лог WARNING")
    logger.error("Лог ERROR")
    logger.critical("Лог CRITICAL")
