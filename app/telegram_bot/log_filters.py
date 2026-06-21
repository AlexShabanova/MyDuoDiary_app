# TODO создать новый пакет filters в app и перенести туда
import logging


class ErrorLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == "ERROR"


class DebugWarningLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname in ("DEBUG", "WARNING")


class CriticalLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == "CRITICAL"
