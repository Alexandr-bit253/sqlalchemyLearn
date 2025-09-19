from config import settings
import asyncio
import asyncpg


async def test_connection():
    try:
        conn = await asyncpg.connect(
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME,
            host=settings.DB_HOST,
            port=settings.DB_PORT
        )
        print("Connection succes!")
        await conn.close()
    except Exception as e:
        print("Error connection:", e)


if __name__ == "__main__":
    asyncio.run(test_connection())
