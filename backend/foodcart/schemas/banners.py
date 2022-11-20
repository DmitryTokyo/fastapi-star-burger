from pydantic import BaseModel, Extra


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


class BannerUpdate(BaseModel):
    title: str | None
    description: str | None
    banner_order: int | None
    image_file: str | None

    class Config:
        extra = Extra.forbid
        orm_mode = True
