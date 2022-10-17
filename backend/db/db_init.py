from backend.config.settings import settings

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

engine = create_async_engine(settings.DB_URL, echo=True)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

Base = declarative_base()
