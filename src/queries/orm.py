from typing import Any

from sqlalchemy import CursorResult, text

from database import engine, session_factory
from models import Worker, metadata_obj


async def print_version_postgresql():
    async with engine.connect() as conn:
        result: CursorResult[Any] = await conn.execute(text("SELECT VERSION()"))
        version = result.scalar()
        print(version)
    await engine.dispose()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(metadata_obj.drop_all)
        await conn.run_sync(metadata_obj.create_all)
    await engine.dispose()


async def insert_data():
    async with session_factory() as session:
        worker_bobr = Worker(username="Bobr")
        worker_volk = Worker(username="Volk")
        session.add_all([worker_bobr, worker_volk])
        await session.commit()
