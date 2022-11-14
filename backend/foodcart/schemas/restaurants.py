from pydantic import BaseModel

from backend.foodcart.schemas.products import ProductOut


class RestaurantBase(BaseModel):
    title: str
    address: str
    contact_phone: str


class RestaurantIn(RestaurantBase):
    pass


class RestaurantOut(RestaurantBase):
    id: int
    longitude: float | None = None
    latitude: float | None = None

    class Config:
        orm_mode = True


class RestaurantMenuItemsBase(BaseModel):
    pass


class RestaurantMenuItemsIn(RestaurantMenuItemsBase):
    product_id: int
    restaurant_id: int


class RestaurantMenuItemsOut(RestaurantMenuItemsBase):
    id: int
    product: ProductOut
    restaurant: RestaurantOut
    available: bool

    class Config:
        orm_mode = True
