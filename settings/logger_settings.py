import logging.config
import socket


class GetHostNameFilter(logging.Filter):
    def filter(self, record):
        record.hostname = socket.getfqdn()
        return True


ERROR_LOG_FILENAME = ".capturadorRTP.log"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] [%(levelname)s] [Capturador RTP] [%(hostname)s] [%(threadName)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "filters": {
        "hostname_filter": {
            "()": "settings.logger_settings.GetHostNameFilter"  # Adjust the module name accordingly
        }
    },
    "handlers": {
        "logfile": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "filename": ERROR_LOG_FILENAME,
            "formatter": "default",
            "backupCount": 2,
            "filters": ["hostname_filter"],
        },
        "verbose_output": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default",
            "stream": "ext://sys.stdout",
            "filters": ["hostname_filter"],
        },
    },
    "loggers": {
        "capturadorRTP": {
            "level": "DEBUG",
            "handlers": [
                "verbose_output",
                "logfile"
            ],
        },
    },
    "root": {"level": "DEBUG", "handlers": ["logfile", "verbose_output"]},
}
