from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from backend.foodcart.crud.base import CRUDBase, ModelType
from backend.foodcart.models.products import Product
from backend.foodcart.models.restaurants import Restaurant, RestaurantMenuItem
from backend.foodcart.schemas.restaurants import RestaurantIn, RestaurantUpdate, RestaurantMenuItemsIn, \
    RestaurantMenuItemUpdate


class CRUDRestaurant(CRUDBase[Restaurant, RestaurantIn, RestaurantUpdate]):
    pass


class CRUDRestaurantItems(CRUDBase[RestaurantMenuItem, RestaurantMenuItemsIn, RestaurantMenuItemUpdate]):
    async def get_multi(self, db: AsyncSession) -> list[ModelType]:
        stmt = select(RestaurantMenuItem).options(
            selectinload(RestaurantMenuItem.product).subqueryload(Product.product_category),
            selectinload(RestaurantMenuItem.restaurant),
        )
        db_execution = await db.execute(stmt)
        return db_execution.scalars().all()

    async def get_single(self, db: AsyncSession, obj_id: int) -> ModelType:
        stmt = select(self.model).where(self.model.id == obj_id).options(
            selectinload(RestaurantMenuItem.product).subqueryload(Product.product_category),
            selectinload(RestaurantMenuItem.restaurant),
        )
        db_execution = await db.execute(stmt)
        return db_execution.scalar_one()


crud_restaurant = CRUDRestaurant(Restaurant)
crud_restaurant_menu_item = CRUDRestaurantItems(RestaurantMenuItem)