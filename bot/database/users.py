from bot.loader import db


class UserRepository:

    @staticmethod
    async def register(user):
        await db.execute(
            """
            INSERT OR IGNORE INTO users (
                user_id,
                username,
                first_name
            )
            VALUES (?, ?, ?)
            """,
            (
                user.id,
                user.username,
                user.first_name
            )
        )

    @staticmethod
    async def get(user_id: int):
        return await db.fetchone(
            "SELECT * FROM users WHERE user_id = ?",
            (user_id,)
        )

    @staticmethod
    async def exists(user_id: int):
        return await UserRepository.get(user_id) is not None