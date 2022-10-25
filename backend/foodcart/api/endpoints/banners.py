from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.db_deps import get_db
from backend.foodcart.schemas.banners import BannerOut, BannerIn
from backend.foodcart.crud.crud_banners import create_banner, get_banners, delete_banner
from backend.foodcart.services.images import save_images

router = APIRouter()


@router.get('/', response_model=list[BannerOut])
async def read_banners(db: AsyncSession = Depends(get_db)) -> list[BannerOut]:
    return await get_banners(db)


@router.post('/', status_code=201)
async def create_new_banner(
    banner_picture: UploadFile,
    banner_in: BannerIn = Depends(),
    db: AsyncSession = Depends(get_db),
) -> dict[str, BannerOut | str]:
    await save_images(banner_picture)
    banner = await create_banner(db, banner_in, banner_picture.filename)
    return {'filename': banner_picture.filename, 'banner': banner}


@router.delete('/', status_code=204)
async def delete_exist_banner(banner_id: int, db: AsyncSession = Depends(get_db)) -> int:
    return await delete_banner(db, banner_id)