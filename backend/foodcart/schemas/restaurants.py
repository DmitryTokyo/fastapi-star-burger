from pydantic import BaseModel


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
