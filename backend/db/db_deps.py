from typing import AsyncGenerator

from backend.db.db_init import async_session


async def get_db() -> AsyncGenerator:
    async with async_session() as session:  # type: ignore
        yield session
