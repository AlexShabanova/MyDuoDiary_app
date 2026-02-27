"""это модуль для тестирования логов с конфигом"""

import logging

logger = logging.getLogger(__name__)


def func_2():
    print("This is func_2")
    logger.debug("Лог DEBUG")
    logger.info("Лог INFO")
    logger.warning("Лог WARNING")
    logger.error("Лог ERROR")
    logger.critical("Лог CRITICAL")
