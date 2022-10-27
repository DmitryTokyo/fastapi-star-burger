from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from backend.foodcart.models.restaurants import Restaurant
from backend.foodcart.schemas.restaurants import RestaurantIn, RestaurantOut


async def get_restaurants(db: AsyncSession) -> list[RestaurantOut]:
    statement = select(Restaurant)
    db_execute = await db.execute(statement)
    return db_execute.scalars().all()


async def create_restaurant(db: AsyncSession, restaurant_in: RestaurantIn) -> Restaurant:
    restaurant_in_data = jsonable_encoder(restaurant_in)
    restaurant_obj = Restaurant(**restaurant_in_data)
    db.add(restaurant_obj)
    await db.commit()
    await db.refresh(restaurant_obj)
    return restaurant_obj


async def delete_restaurant(db: AsyncSession, restaurant_id: int) -> int:
    stmt = delete(Restaurant).where(Restaurant.id == restaurant_id)
    await db.execute(stmt)
    await db.commit()
