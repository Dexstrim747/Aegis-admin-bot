from bot.loader import db


class WarnRepository:

    @staticmethod
    async def add(
        chat_id: int,
        user_id: int,
        admin_id: int,
        reason: str
    ):
        await db.execute(
            """
            INSERT INTO warns (
                chat_id,
                user_id,
                admin_id,
                reason
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                chat_id,
                user_id,
                admin_id,
                reason
            )
        )

    @staticmethod
    async def count(chat_id: int, user_id: int):
        row = await db.fetchone(
            """
            SELECT COUNT(*)
            FROM warns
            WHERE chat_id = ?
            AND user_id = ?
            """,
            (
                chat_id,
                user_id
            )
        )

        return row[0]