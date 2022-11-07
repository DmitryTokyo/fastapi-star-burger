from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_200_OK

from backend.db.db_deps import get_db
from backend.foodcart.schemas.banners import BannerOut, BannerIn
from backend.foodcart.crud.crud_banners import create_banner, get_banners, delete_banner
from backend.star_burger.utils.images import save_image

router = APIRouter()


@router.get('/', response_model=list[BannerOut], status_code=HTTP_200_OK)
async def read_banners(db: AsyncSession = Depends(get_db)):
    return await get_banners(db)


@router.post('/', status_code=HTTP_201_CREATED)
async def create_new_banner(
    banner_picture: UploadFile,
    banner_in: BannerIn = Depends(),
    db: AsyncSession = Depends(get_db),
) -> dict[str, BannerOut | str]:
    await save_image(banner_picture)
    banner = await create_banner(db, banner_in, banner_picture.filename)
    return {'filename': banner_picture.filename, 'banner': banner}


@router.delete('/', status_code=HTTP_204_NO_CONTENT)
async def delete_exist_banner(banner_id: int, db: AsyncSession = Depends(get_db)) -> None:
    await delete_banner(db, banner_id)
