from typing import AsyncGenerator

from sqlalchemy import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker,
)

from backend.config import settings


async_engine = create_async_engine(
    settings.SQLALCHEMY_ASYNC_DATABASE_URI,
    pool_pre_ping=True,
    poolclass=AsyncAdaptedQueuePool,
    pool_size=500,
    max_overflow=50,
    echo=True,
)

async_session = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    expire_on_commit=False,
)

async def get_db() -> AsyncGenerator:
    async with async_session() as session:
        yield session
