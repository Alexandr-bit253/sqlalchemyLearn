from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from config import settings

engine: AsyncEngine = create_async_engine(url=settings.DATABASE_URL_asyncpg, echo=False)


session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass
