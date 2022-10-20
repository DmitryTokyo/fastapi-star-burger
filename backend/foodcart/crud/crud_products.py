from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.foodcart.models.products import Product, ProductCategory
from backend.foodcart.schemas.products import ProductIn, ProductCategoryIn


async def get_products(db: AsyncSession) -> list[Product]:
    statement = select(Product)
    db_execute = await db.execute(statement)
    return db_execute.scalars().all()


async def create_product(db: AsyncSession, restaurant_in: ProductIn, picture_filename: str) -> Product:
    product_in_data = jsonable_encoder(restaurant_in)
    product_in_data |= {'image_file': picture_filename}
    product_obj = Product(**product_in_data)
    db.add(product_obj)
    await db.commit()
    await db.refresh(product_obj)
    return product_obj


async def get_product_categories(db: AsyncSession) -> list[ProductCategory]:
    statement = select(ProductCategory)
    db_execute = await db.execute(statement)
    return db_execute.scalars().all()


async def create_product_category(db: AsyncSession, product_category_in: ProductCategoryIn) -> list[ProductCategoryIn]:
    product_category_in_data = jsonable_encoder(product_category_in)
    product_category_obj = ProductCategory(**product_category_in_data)
    db.add(product_category_obj)
    await db.commit()
    await db.refresh(product_category_obj)
    return product_category_obj
