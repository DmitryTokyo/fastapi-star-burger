from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db.db_deps import get_db
from backend.foodcart.schemas.banners import BannerOut, BannerIn
from backend.foodcart.crud.crud_banners import get_banners, create_banner

router = APIRouter()


@router.get("/", response_model=list[BannerOut])
def read_banners(db: Session = Depends(get_db)) -> list[BannerOut]:
    banners = get_banners(db)
    return banners


@router.post('/', response_model=BannerIn, status_code=201)
def create_new_banner(banner_in: BannerIn, db: Session = Depends(get_db)) -> BannerOut:
    banner = create_banner(db, banner_in)
    return banner
