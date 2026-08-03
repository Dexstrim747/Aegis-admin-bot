from bot.loader import db


class SettingsRepository:

    @staticmethod
    async def get(chat_id: int):
        return await db.fetchone(
            """
            SELECT *
            FROM settings
            WHERE chat_id = ?
            """,
            (chat_id,)
        )

    @staticmethod
    async def create(chat_id: int):
        await db.execute(
            """
            INSERT OR IGNORE INTO settings (
                chat_id
            )
            VALUES (?)
            """,
            (chat_id,)
        )