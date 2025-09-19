from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from config import settings

engine: AsyncEngine = create_async_engine(url=settings.DATABASE_URL_asyncpg, echo=False)
