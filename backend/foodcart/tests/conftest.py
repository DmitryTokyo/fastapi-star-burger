import asyncio
from sqlalchemy import select

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from backend.db.db_init import Base
from backend.foodcart.schemas.banners import BannerOut
from backend.server import app


TESL_DB_URL = 'sqlite+aiosqlite:///:memory:'


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='module')
async def test_db_engine(event_loop):
    test_engine = create_async_engine(TESL_DB_URL, echo=False)
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
    yield test_engine
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await test_engine.dispose()


@pytest_asyncio.fixture(scope='module')
async def test_session(test_db_engine):
    async_test_session = sessionmaker(test_db_engine, class_=AsyncSession, expire_on_commit=False)
    async with async_test_session() as session:
        yield session


@pytest_asyncio.fixture(scope='function')
async def insert_object_to_db(test_session):
    async def _insert_query(query_config, model):
        execution_result = await test_session.execute(query_config)
        await test_session.commit()
        session_execution = await test_session.execute(
            select(model).where(model.id == execution_result.inserted_primary_key[0]),
        )
        return session_execution.scalar_one()
    return _insert_query


@pytest_asyncio.fixture(scope='function')
async def get_all_object_from_db(test_session):
    async def _get_query(query):
        result = await test_session.execute(query)
        return result.scalars().all()
    return _get_query


@pytest_asyncio.fixture(scope='function')
async def get_single_object_from_db(test_session):
    async def _get_query(query):
        result = await test_session.execute(query)
        return result.scalar_one()
    return _get_query


@pytest_asyncio.fixture(scope='module')
async def async_client():
    async with AsyncClient(app=app, base_url='https://') as client:
        yield client


@pytest_asyncio.fixture
def banner_schema():
    return BannerOut(title='test title', description='test description', banner_order=1, id=1, image_file='image.jpg')
