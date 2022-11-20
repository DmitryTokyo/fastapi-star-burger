from decimal import Decimal

from pydantic import BaseModel, Extra


class ProductCategoryBase(BaseModel):
    title: str


class ProductCategoryIn(ProductCategoryBase):
    pass


class ProductCategoryOut(ProductCategoryBase):
    id: int

    class Config:
        orm_mode = True


class ProductCategoryUpdate(BaseModel):
    title: str | None

    class Config:
        extra = Extra.forbid
        orm_mode = True


class ProductBase(BaseModel):
    title: str
    price: Decimal


class ProductIn(ProductBase):
    ingredients: str | None
    product_category_id: int


class ProductOut(ProductBase):
    id: int
    special_status: bool
    product_category: ProductCategoryOut
    image_url: str

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    title: str | None
    price: Decimal
    ingredients: str | None
    product_category_id: int | None
    special_status: bool | None
    image_url: str | None

    class Config:
        extra = Extra.forbid
        orm_mode = True
