from aiogram import Bot
from aiogram.types import Message

from bot.database.warns import WarnRepository


class ModerationService:

    @staticmethod
    async def warn(bot: Bot, message: Message):

        if not message.reply_to_message:
            await message.answer(
                "⚠️ Используйте команду ответом на сообщение пользователя."
            )
            return

        target = message.reply_to_message.from_user

        reason = message.text.removeprefix("/warn").strip()

        if not reason:
            reason = "Причина не указана."

        await WarnRepository.add(
            message.chat.id,
            target.id,
            message.from_user.id,
            reason
        )

        warns = await WarnRepository.count(
            message.chat.id,
            target.id
        )

        await message.answer(
            f"⚠️ Пользователь получил предупреждение.\n\n"
            f"Причина: {reason}\n"
            f"Всего предупреждений: {warns}"
        )