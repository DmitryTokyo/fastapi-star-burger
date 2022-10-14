from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from backend.foodcart.models.banners import Banner
from backend.foodcart.schemas.banners import BannerIn


def get_banners(db: Session):
    return db.query(Banner).all()


def create_banner(db: Session, banner_in: BannerIn):
    banner_in_data = jsonable_encoder(banner_in)
    banner_obj = Banner(**banner_in_data)
    db.add(banner_obj)
    db.commit()
    db.refresh(banner_obj)
    return banner_obj
