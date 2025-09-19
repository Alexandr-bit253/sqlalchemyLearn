import asyncio
from typing import Any

from sqlalchemy import CursorResult, text
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from config import settings

engine: AsyncEngine = create_async_engine(url=settings.DATABASE_URL_asyncpg, echo=False)


async def print_version_postgresql():
    async with engine.connect() as conn:
        result: CursorResult[Any] = await conn.execute(text("SELECT VERSION()"))
        version = result.scalar()
        print(version)
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(print_version_postgresql())
