import aiosqlite

import os

class Database:
    def __init__(self, path: str = "data/aegis.db"):
        self.path = path
        self.connection = None

    async def connect(self):
        self.connection = await aiosqlite.connect(self.path)
        await self.connection.execute("PRAGMA foreign_keys = ON;")
        await self.connection.commit()
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    async def close(self):
        if self.connection:
            await self.connection.close()

    async def execute(self, query: str, params: tuple = ()):
        await self.connection.execute(query, params)
        await self.connection.commit()

    async def fetchone(self, query: str, params: tuple = ()):
        cursor = await self.connection.execute(query, params)
        return await cursor.fetchone()

    async def fetchall(self, query: str, params: tuple = ()):
        cursor = await self.connection.execute(query, params)
        return await cursor.fetchall()