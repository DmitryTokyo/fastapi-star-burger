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


class ProductIn(ProductBase):
    ingredients: str | None
    product_category_id: int


class ProductOut(ProductBase):
    id: int
    special_status: bool
    product_category: ProductCategoryOut

    class Config:
        orm_mode = True
