from fastapi import APIRouter, Depends
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_200_OK

from backend.db.db_deps import get_db
from backend.foodcart.crud.crud_restaurants import get_restaurants, create_restaurant, delete_restaurant
from backend.foodcart.schemas.restaurants import RestaurantOut, RestaurantIn

router = APIRouter()


@router.get('/', response_model=list[RestaurantOut], status_code=HTTP_200_OK)
async def read_restaurants(db: AsyncSession = Depends(get_db)):
    return await get_restaurants(db)


@router.post('/', response_model=RestaurantOut, status_code=HTTP_201_CREATED)
async def create_new_restaurant(restaurant_in: RestaurantIn, db: AsyncSession = Depends(get_db)):
    return await create_restaurant(db, restaurant_in)


@router.delete('/', status_code=HTTP_204_NO_CONTENT)
async def delete_exist_restaurant(restaurant_id: int, db: AsyncSession = Depends(get_db)) -> None:
    await delete_restaurant(db, restaurant_id)
