from typing import Any

from sqlalchemy import CursorResult, text

from database import engine
from models import metadata_obj


async def print_version_postgresql():
    async with engine.connect() as conn:
        result: CursorResult[Any] = await conn.execute(text("SELECT VERSION()"))
        version = result.scalar()
        print(version)
    await engine.dispose()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(metadata_obj.create_all)
