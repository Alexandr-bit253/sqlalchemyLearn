from typing import Any

from sqlalchemy import CursorResult, insert, text

from database import engine
from models import metadata_obj, workers_table


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
    async with engine.connect() as conn:
        # sql
        # stmt = """INSERT INTO employer (username) VALUES
        #             ('Bobr'),
        #             ('Volk');"""

        # query builder
        stmt = insert(workers_table).values(
            [
                {"username": "Bobr"},
                {"username": "Volk"},
            ]
        )
        await conn.execute(stmt)
        await conn.commit()
    await engine.dispose()
