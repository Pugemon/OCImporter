import sys
import asyncio
import asyncmy

from loguru import logger
from tortoise import Tortoise

from config import settings

# Remove the existing logger
logger.remove()
# Add a new logger with the given settings
logger.add(
    sys.stdout,
    colorize=settings.get("logging.colorize"),
    level=settings.get("logging.level"),
    format=settings.get("logging.format"),
)
# Add logging to file
logger.add(
    settings.get("logging.file_path"),
    level=settings.get("logging.level"),
    format=settings.get("logging.format"),
    rotation=settings.get("logging.rotation"),
    enqueue=settings.get("logging.enqueue"),
)


async def init_db():
    await Tortoise.init(
        db_url=settings.db.url,
    )
