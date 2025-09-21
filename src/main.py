import asyncio
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))

from database import engine

# from queries.core import create_tables, insert_data
from queries.orm import create_tables, insert_data


async def main():
    await create_tables()
    await insert_data()
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
