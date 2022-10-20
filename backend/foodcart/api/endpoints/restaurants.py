from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.db_deps import get_db
from backend.foodcart.crud.crud_restaurants import get_restaurants, create_restaurant
from backend.foodcart.schemas.restaurants import RestaurantOut, RestaurantIn

router = APIRouter()


@router.get('/', response_model=list[RestaurantOut])
async def read_restaurants(db: AsyncSession = Depends(get_db)) -> list[RestaurantOut]:
    return await get_restaurants(db)


@router.post('/', response_model=RestaurantIn, status_code=201)
async def create_new_restaurant(restaurant_in: RestaurantIn, db: AsyncSession = Depends(get_db)) -> RestaurantOut:
    return await create_restaurant(db, restaurant_in)
