from loguru import logger# from logging.handlers import RotatingFileHandler
from conf.config import settings
import os
log_dir = settings.LOGGER_DIR
    
logger.add(
    sink=f"{log_dir}/app.log",
    enqueue=True,
    rotation="4 weeks",
    retention="4 months",
    encoding="utf-8",
    backtrace=True,
    level=settings.LOGGER_LEVEL,
    diagnose=True,
)