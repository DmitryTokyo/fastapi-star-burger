import aiofiles
from fastapi import APIRouter, Depends, UploadFile, File, Form
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from backend.db.db_deps import get_db
from backend.foodcart.schemas.banners import BannerOut, BannerIn
from backend.foodcart.crud.crud_banners import create_banner, get_banners
from backend.foodcart.utils.save_file import save_images_to_media

router = APIRouter()


@router.get('/', response_model=list[BannerOut])
async def read_banners(db: Session = Depends(get_db)) -> list[BannerOut]:
    banners = await get_banners(db)
    return banners


@router.post('/', status_code=201)
async def create_new_banner(
    banner_picture: UploadFile,
    banner_in: BannerIn = Depends(),
    db: Session = Depends(get_db),
) -> BannerOut:
    await save_images_to_media(banner_picture)
    banner = await create_banner(db, banner_in, banner_picture.filename)
    return {'filename': banner_picture.filename, 'banner': banner}
