from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.database.users import UserRepository

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await UserRepository.register(message.from_user)

    await message.answer(
        "🛡️ Добро пожаловать в Aegis!\n\n"
        "Бот находится в разработке."
    )