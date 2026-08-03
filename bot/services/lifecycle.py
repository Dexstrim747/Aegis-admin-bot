from bot.loader import db
from bot.database.models import CREATE_TABLES
from bot.utils.logger import logger


async def startup():
    logger.info("Подключение базы данных...")

    await db.connect()

    for table in CREATE_TABLES:
        await db.execute(table)

    logger.info("База данных готова.")


async def shutdown():
    logger.info("Отключение базы данных...")

    await db.close()

    logger.info("Aegis остановлен.")