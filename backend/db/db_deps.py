from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.db_init import async_session


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
