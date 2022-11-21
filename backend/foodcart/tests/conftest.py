import pytest
from httpx import AsyncClient

from backend.foodcart.schemas.banners import BannerOut
from backend.server import app


@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url='https://') as client:
        yield client


@pytest.fixture
def banner_schema():
    return BannerOut(title='test title', description='test description', banner_order=1, id=1, image_file='image.jpg')
