from aiogram import BaseMiddleware

from bot.database.users import UserRepository
from bot.database.chats import ChatRepository
from bot.database.settings import SettingsRepository


class DatabaseMiddleware(BaseMiddleware):

    async def __call__(self, handler, event, data):

        if hasattr(event, "from_user") and event.from_user:
            await UserRepository.register(event.from_user)

        if hasattr(event, "chat") and event.chat.type != "private":
            await ChatRepository.register(event.chat)
            await SettingsRepository.create(event.chat.id)

        return await handler(event, data)