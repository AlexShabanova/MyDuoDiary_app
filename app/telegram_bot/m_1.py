"""это модуль для тестирования логов с конфигом"""

import logging

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)
print(__name__)


def func_1():
    print("This is func_1")
    logger.debug("Лог DEBUG")
    logger.info("Лог INFO")
    logger.warning("Лог WARNING")
    logger.error("Лог ERROR")
    logger.critical("Лог CRITICAL")
