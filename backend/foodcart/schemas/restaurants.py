from pydantic import BaseModel


class RestaurantBase(BaseModel):
    title: str
    address: str


class RestaurantIn(RestaurantBase):
    contact_phone: str


class RestaurantOut(RestaurantBase):
    id: int
    longitude: float
    latitude: float
    