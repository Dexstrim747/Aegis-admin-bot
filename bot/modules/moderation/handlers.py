from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.filters import IsAdmin
from bot.modules.moderation.service import ModerationService

router = Router()


@router.message(Command("warn"), IsAdmin())
async def warn(message: Message):
    await ModerationService.warn(message.bot, message)