from bot.loader import db


class ChatRepository:

    @staticmethod
    async def register(chat):
        await db.execute(
            """
            INSERT OR IGNORE INTO chats (
                chat_id,
                title
            )
            VALUES (?, ?)
            """,
            (
                chat.id,
                chat.title
            )
        )

    @staticmethod
    async def get(chat_id: int):
        return await db.fetchone(
            "SELECT * FROM chats WHERE chat_id = ?",
            (chat_id,)
        )