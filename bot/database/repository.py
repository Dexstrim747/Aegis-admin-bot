from bot.loader import db


class UserRepository:

    @staticmethod
    async def add_user(user):
        await db.execute(
            """
            INSERT OR IGNORE INTO users(user_id, username, first_name)
            VALUES (?, ?, ?)
            """,
            (
                user.id,
                user.username,
                user.first_name
            )
        )