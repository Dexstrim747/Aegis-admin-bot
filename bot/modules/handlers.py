from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("ban"))
async def ban(message: Message):
    await message.answer(
        "🚧 Команда /ban пока находится в разработке."
    )


@router.message(Command("mute"))
async def mute(message: Message):
    await message.answer(
        "🚧 Команда /mute пока находится в разработке."
    )


@router.message(Command("kick"))
async def kick(message: Message):
    await message.answer(
        "🚧 Команда /kick пока находится в разработке."
    )