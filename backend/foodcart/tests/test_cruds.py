from sqlalchemy import insert

from backend.foodcart.crud.crud_banners import get_banners
from backend.foodcart.models.banners import Banner
from backend.foodcart.schemas.banners import BannerOut


async def test_get_banners(insert_query_to_db, test_session):
    stmt = insert(Banner).values(
        title='test_title', description='test description', banner_order=1, image_file='test.jpg',
    )
    await insert_query_to_db(stmt)

    banners = await get_banners(test_session)
    banner_out = BannerOut.from_orm(banners[0])

    assert len(banners) == 1
    assert banner_out.dict() == {
        'title': 'test_title',
        'description': 'test description',
        'banner_order': 1,
        'image_file': 'test.jpg',
        'id': banners[0].id,
    }
