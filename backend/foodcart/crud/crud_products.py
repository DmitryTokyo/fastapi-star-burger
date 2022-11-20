from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from backend.foodcart.models.products import Product, ProductCategory
from backend.foodcart.schemas.products import ProductIn, ProductCategoryIn, ProductCategoryUpdate


async def get_products(db: AsyncSession) -> list[Product]:
    stmt = select(Product).options(selectinload(Product.product_category))
    db_execute = await db.execute(stmt)
    return db_execute.scalars().all()


async def create_product(db: AsyncSession, restaurant_in: ProductIn, picture_filename: str) -> Product:
    product_in_data = jsonable_encoder(restaurant_in)
    product_in_data |= {'image_url': picture_filename}
    product_obj = Product(**product_in_data)
    db.add(product_obj)
    await db.commit()
    await db.refresh(product_obj)
    return product_obj


async def delete_product(db: AsyncSession, product_id: int) -> None:
    stmt = delete(Product).where(Product.od == product_id)
    await db.execute(stmt)
    await db.commit()


async def get_product_categories(db: AsyncSession) -> list[ProductCategory]:
    stmt = select(ProductCategory)
    db_execute = await db.execute(stmt)
    return db_execute.scalars().all()


async def create_product_category(db: AsyncSession, product_category_in: ProductCategoryIn) -> ProductCategory:
    product_category_in_data = jsonable_encoder(product_category_in)
    product_category_obj = ProductCategory(**product_category_in_data)
    db.add(product_category_obj)
    await db.commit()
    await db.refresh(product_category_obj)
    return product_category_obj


async def delete_product_category(db: AsyncSession, product_category_id: int) -> None:
    stmt = delete(ProductCategory).where(ProductCategory.id == product_category_id)
    await db.execute(stmt)
    await db.commit()


async def update_product_category(
        db: AsyncSession,
        product_category_id: int,
        product_category_update: ProductCategoryUpdate
) -> ProductCategory:
    product_category_update_data = product_category_update.dict(exclude_unset=True)
    stmt = update(ProductCategory).where(ProductCategory.id == product_category_id).values(product_category_update_data)
    await db.execute(stmt)
    await db.commit()

    stmt = select(ProductCategory).where(ProductCategory.id == product_category_id)
    db_execute = await db.execute(stmt)
    return db_execute.scalar_one()
