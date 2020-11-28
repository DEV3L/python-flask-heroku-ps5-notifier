import logging
import os
import sys
from logging.handlers import RotatingFileHandler

ten_megabytes = 10 * 1024 * 1024

default_logging_format = os.getenv('LOGGING_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
default_level = os.getenv('LOGGING_LEVEL', logging.INFO)
default_max_bytes = os.getenv('LOGGING_MAX_BYTES', ten_megabytes)
default_backup_count = os.getenv('LOGGING_BACKUP_COUNT', 5)
default_path = os.getenv('LOGGING_PATH', 'logs/python-flask-heroku-ps5-notifier.log')


class LoggingService:
    def __init__(self, name: str, *, logging_format: str = default_logging_format, level: int = default_level,
                 max_bytes: int = default_max_bytes, backup_count: int = default_backup_count,
                 path: str = default_path):
        self.name = name
        self.logging_format = logging_format
        self.level = level
        self.max_bytes = int(max_bytes)
        self.backup_count = int(backup_count)
        self.path = path

        self._logger = None

    @property
    def logger(self):
        if self._logger:
            return self._logger

        self._logger = self._build_logger()
        return self._logger

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def exception(self, message):
        self.logger.exception(message)

    @property
    def formatter(self):
        return logging.Formatter(self.logging_format, datefmt='%Y-%m-%d %H:%M:%S')

    def _build_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)

        sys_stdout_stream_handler = self._build_sys_stdout_stream_handler()
        logger.addHandler(sys_stdout_stream_handler)

        rotating_file_handler = self._build_rotating_file_handler()
        logger.addHandler(rotating_file_handler)

        return logger

    def _build_sys_stdout_stream_handler(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(self.level)
        stream_handler.setFormatter(self.formatter)

        return stream_handler

    def _build_rotating_file_handler(self):
        rotating_file_handler = RotatingFileHandler(self.path, maxBytes=self.max_bytes, backupCount=self.backup_count)
        rotating_file_handler.setLevel(self.level)
        rotating_file_handler.setFormatter(self.formatter)

        return rotating_file_handler
