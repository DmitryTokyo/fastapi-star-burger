from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from backend.foodcart.crud.base import CRUDBase, ModelType
from backend.foodcart.models.products import Product, ProductCategory
from backend.foodcart.schemas.products import ProductIn, ProductUpdate, ProductCategoryIn, ProductCategoryUpdate


class CRUDProduct(CRUDBase[Product, ProductIn, ProductUpdate]):
    async def get_multi(self, db: AsyncSession) -> list[ModelType]:
        stmt = select(self.model).options(selectinload('product_category'))
        db_execution = await db.execute(stmt)
        return db_execution.scalars().all()


class CRUDProductCategory(CRUDBase[ProductCategory, ProductCategoryIn, ProductCategoryUpdate]):
    pass


crud_product = CRUDProduct(Product)
crud_product_category = CRUDProductCategory(ProductCategory)
