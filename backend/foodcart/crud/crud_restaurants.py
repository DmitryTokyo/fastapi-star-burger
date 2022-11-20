from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from backend.foodcart.models.products import Product
from backend.foodcart.models.restaurants import Restaurant, RestaurantMenuItem
from backend.foodcart.schemas.restaurants import (
    RestaurantIn, RestaurantOut, RestaurantMenuItemsOut, RestaurantMenuItemsIn, RestaurantUpdate,
    RestaurantMenuItemUpdate,
)


async def get_restaurants(db: AsyncSession) -> list[RestaurantOut]:
    stmt = select(Restaurant)
    db_execute = await db.execute(stmt)
    return db_execute.scalars().all()


async def create_restaurant(db: AsyncSession, restaurant_in: RestaurantIn) -> Restaurant:
    restaurant_in_data = jsonable_encoder(restaurant_in)
    restaurant_obj = Restaurant(**restaurant_in_data)
    db.add(restaurant_obj)
    await db.commit()
    await db.refresh(restaurant_obj)
    return restaurant_obj


async def update_restaurant(db: AsyncSession, restaurant_update: RestaurantUpdate, restaurant_id: int):
    restaurant_data = restaurant_update.dict(exclude_unset=True)
    stmt = update(Restaurant).where(Restaurant.id == restaurant_id).values(restaurant_data)
    await db.execute(stmt)
    await db.commit()

    stmt = select(Restaurant).where(Restaurant.id == restaurant_id)
    db_execute = await db.execute(stmt)
    return db_execute.scalar_one()


async def delete_restaurant(db: AsyncSession, restaurant_id: int) -> None:
    stmt = delete(Restaurant).where(Restaurant.id == restaurant_id)
    await db.execute(stmt)
    await db.commit()


async def get_restaurant_items(db: AsyncSession) -> list[RestaurantMenuItemsOut]:
    stmt = select(RestaurantMenuItem).options(
        selectinload(RestaurantMenuItem.product).subqueryload(Product.product_category),
        selectinload(RestaurantMenuItem.restaurant),
    )
    db_execute = await db.execute(stmt)
    return db_execute.scalars().all()


async def create_restaurant_menu_item(
        db: AsyncSession,
        restaurant_menu_item_in: RestaurantMenuItemsIn,
) -> RestaurantMenuItem:
    restaurant_menu_item_in_data = jsonable_encoder(restaurant_menu_item_in)
    restaurant_menu_item_obj = RestaurantMenuItem(**restaurant_menu_item_in_data)
    db.add(restaurant_menu_item_obj)
    await db.commit()
    await db.refresh(restaurant_menu_item_obj)
    return restaurant_menu_item_obj


async def delete_restaurant_menu_item(db: AsyncSession, restaurant_menu_item_id: int) -> None:
    stmt = delete(RestaurantMenuItem).where(RestaurantMenuItem.id == restaurant_menu_item_id)
    await db.execute(stmt)
    await db.commit()


async def update_restaurant_menu_item(
    db: AsyncSession,
    restaurant_menu_item_update: RestaurantMenuItemUpdate,
    restaurant_menu_item_id: int,
) -> RestaurantMenuItem:
    restaurant_menu_item_data = restaurant_menu_item_update.dict(exclude_unset=True)
    stmt = update(
        RestaurantMenuItem
    ).where(RestaurantMenuItem.id == restaurant_menu_item_id).values(restaurant_menu_item_data)
    await db.execute(stmt)
    await db.commit()

    stmt = select(RestaurantMenuItem).where(RestaurantMenuItem.id == restaurant_menu_item_id)
    db_execute = await db.execute(stmt)
    return db_execute.scalar_one()
