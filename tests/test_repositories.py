import pytest

from bot.database.database import Database


@pytest.mark.asyncio
async def test_create_database():

    db = Database("data/tests/test.db")

    await db.connect()

    await db.execute(
        """
        CREATE TABLE IF NOT EXISTS test(
            id INTEGER PRIMARY KEY
        )
        """
    )

    result = await db.fetchone(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='test';"
    )

    assert result is not None

    await db.close()