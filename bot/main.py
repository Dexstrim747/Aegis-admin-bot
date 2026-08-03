from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession

from bot.config import BOT_TOKEN
from bot.loader import dp
from bot.middlewares.database import DatabaseMiddleware
from bot.services.lifecycle import startup, shutdown
from bot.utils.logger import logger
from bot.utils.router_loader import register_all_routers


async def main():
    if not BOT_TOKEN:
        logger.warning("BOT_TOKEN отсутствует.")
        logger.info("Архитектура проекта успешно загружена.")
        return

    session = AiohttpSession(
        proxy="socks5://127.0.0.1:3067"
    )

    bot = Bot(
        token=BOT_TOKEN,
        session=session
    )

    register_all_routers(dp)

    await startup()

    try:
        logger.info("Запуск Aegis...")
        await dp.start_polling(bot)

    finally:
        await bot.session.close()
        await shutdown()