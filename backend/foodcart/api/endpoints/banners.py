from fastapi import APIRouter, Depends, UploadFile, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from backend.db.db_deps import get_db
from backend.foodcart.schemas.banners import BannerOut, BannerIn, BannerUpdate
from backend.star_burger.utils.images import save_image_to_server
from backend.foodcart.crud.banner import crud_banner

router = APIRouter()


@router.get('/', response_model=list[BannerOut], status_code=HTTP_200_OK)
async def read_banners(db: AsyncSession = Depends(get_db)):
    return await crud_banner.get_multi(db)


@router.post('/', status_code=HTTP_201_CREATED)
async def create_new_banner(
    banner_picture: UploadFile,
    banner_in: BannerIn = Depends(),
    db: AsyncSession = Depends(get_db),
) -> dict[str, BannerOut | str]:
    await save_image_to_server(banner_picture)
    banner = await crud_banner.create(db, banner_in, image_file=banner_picture.filename)
    return {'filename': banner_picture.filename, 'banner': banner}


@router.delete('/', status_code=HTTP_200_OK)
async def delete_exist_banner(banner_id: int, db: AsyncSession = Depends(get_db)) -> dict[str, int]:
    try:
        await crud_banner.get_single(db, banner_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Object does not found')
    deleted_banner_id = await crud_banner.delete(db, banner_id)
    return {'deleted banner id': deleted_banner_id}


@router.patch('/{banner_id}/image', response_model=BannerOut, status_code=HTTP_200_OK)
async def update_exist_banner_image(
    banner_id: int,
    banner_image: UploadFile,
    db: AsyncSession = Depends(get_db),
):
    try:
        await crud_banner.get_single(db, banner_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Object does not found')

    await save_image_to_server(banner_image)
    banner_update = BannerUpdate(image_file=banner_image.filename)
    return await crud_banner.update(db, banner_update, banner_id)


@router.patch('/{banner_id}', response_model=BannerOut, status_code=HTTP_200_OK)
async def update_exist_banner(
    banner_id: int,
    banner_update: BannerUpdate,
    db: AsyncSession = Depends(get_db),
):
    try:
        await crud_banner.get_single(db, banner_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Object does not found')

    return await crud_banner(db, banner_update, banner_id)
