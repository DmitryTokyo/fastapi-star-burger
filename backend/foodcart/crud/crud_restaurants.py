from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.foodcart.models.restaurants import Restaurant
from backend.foodcart.schemas.restaurants import RestaurantIn


async def get_restaurants(db: AsyncSession) -> list[Restaurant]:
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
