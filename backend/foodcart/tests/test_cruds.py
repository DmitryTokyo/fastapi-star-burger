import pytest
from sqlalchemy import insert, select

from backend.foodcart.crud.banner import crud_banner
from backend.foodcart.models.banners import Banner
from backend.foodcart.schemas.banners import BannerOut, BannerIn, BannerUpdate


async def test_get_banners(insert_object_to_db, test_session):
    stmt = insert(Banner).values(
        title='test_title', description='test description', banner_order=1, image_file='test.jpg',
    )
    expected_result = BannerOut(
        title='test_title',
        description='test description',
        banner_order=1,
        image_file='test.jpg',
        id=1,
    )
    await insert_object_to_db(stmt, Banner)

    banners = await crud_banner.get_multi(test_session)
    banner_out = BannerOut.from_orm(banners[0])

    assert len(banners) == 1
    assert banner_out == expected_result


@pytest.mark.parametrize(
    'banner_in, picture_filename',
    [
        (BannerIn(title='test banner title', description='test banner description', banner_order=2), 'banner.jpg'),
        (BannerIn(title='test one more banner title', description='test ', banner_order=3), 'banner_one_more.jpg'),
    ],
)
async def test_create_banner(test_session, get_all_object_from_db, banner_in, picture_filename):
    banner = await crud_banner.create(test_session, banner_in, image_file=picture_filename)
    expected_objects = await get_all_object_from_db(select(Banner).where(Banner.id == banner.id))

    assert banner == expected_objects[0]
    assert banner.id == expected_objects[0].id


async def test_delete_banner(insert_object_to_db, test_session, get_all_object_from_db):
    stmt = insert(Banner).values(
        title='test_title', description='test description', banner_order=1, image_file='test.jpg',
    )
    await insert_object_to_db(stmt, Banner)

    await crud_banner.delete(test_session, 1)
    expected_objects = await get_all_object_from_db(select(Banner).where(Banner.id == 1))

    assert len(expected_objects) == 0


async def test_update_banner(insert_object_to_db, test_session):
    stmt = insert(Banner).values(
        title='test_title', description='test description', banner_order=1, image_file='test.jpg',
    )
    initial_obj = await insert_object_to_db(stmt, Banner)
    banner_update = BannerUpdate(title='updated_title')
    await crud_banner.update(test_session, banner_update, initial_obj.id)
    assert banner_update.title == 'updated_title'
