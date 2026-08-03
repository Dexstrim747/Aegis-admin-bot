import logging
import os

import colorlog

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("Aegis")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(log_color)s[%(asctime)s] %(levelname)s | %(message)s",
        datefmt="%H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )
)

file_handler = logging.FileHandler(
    "logs/latest.log",
    encoding="utf-8"
)
file_handler.setFormatter(
    logging.Formatter(
        "[%(asctime)s] %(levelname)s | %(message)s",
        datefmt="%d.%m.%Y %H:%M:%S",
    )
)

logger.addHandler(console_handler)
logger.addHandler(file_handler)