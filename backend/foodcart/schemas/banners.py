from pydantic import BaseModel


class BannerBase(BaseModel):
    title: str
    description: str | None = None
    banner_order: int


class BannerIn(BannerBase):
    pass


class BannerOut(BannerBase):
    id: int
    image_file: str

    class Config:
        orm_mode = True
