from bot.database.database import Database

import pytest


@pytest.mark.asyncio
async def test_database_connection():

    db = Database("data/tests/test.db")

    await db.connect()

    assert db.connection is not None

    await db.close()