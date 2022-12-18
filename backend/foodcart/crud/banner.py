from backend.foodcart.crud.base import CRUDBase
from backend.foodcart.models.banners import Banner
from backend.foodcart.schemas.banners import BannerIn, BannerUpdate


class CRUDBanner(CRUDBase[Banner, BannerIn, BannerUpdate]):
    pass


crud_banner = CRUDBanner(Banner)
