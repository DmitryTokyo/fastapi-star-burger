from decimal import Decimal

from pydantic import BaseModel


class ProductCategoryBase(BaseModel):
    title: str


class ProductCategoryIn(ProductCategoryBase):
    pass


class ProductCategoryOut(ProductCategoryBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    title: str
    price: Decimal
    image_url: str
    product_category: ProductCategoryOut


class ProductIn(ProductBase):
    ingredients: str | None


class ProductOut(ProductBase):
    id: int
    special_status: bool

    class Config:
        orm_mode = True
