import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger("SmartSurveillance")
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler("logs/system.log", maxBytes=2_000_000, backupCount=3)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

