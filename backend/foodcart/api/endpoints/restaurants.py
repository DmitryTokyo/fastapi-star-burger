from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_200_OK

from backend.db.db_deps import get_db
from backend.foodcart.crud.crud_restaurants import (
    get_restaurants, create_restaurant, delete_restaurant, get_restaurant_items, create_restaurant_menu_item,
    delete_restaurant_menu_item, update_restaurant, update_restaurant_menu_item,
)
from backend.foodcart.schemas.restaurants import (
    RestaurantOut, RestaurantIn, RestaurantMenuItemsOut, RestaurantMenuItemsIn, RestaurantUpdate,
    RestaurantMenuItemUpdate,
)

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


@router.patch('/{restaurant_id}', response_model=RestaurantOut, status_code=HTTP_200_OK)
async def update_exist_restaurant(
        restaurant_id: int,
        restaurant_update_in: RestaurantUpdate,
        db: AsyncSession = Depends(get_db),
):
    updated_restaurant_obj = await update_restaurant(db, restaurant_update_in, restaurant_id)
    return updated_restaurant_obj


@router.get('/restaurant-menu-items', response_model=list[RestaurantMenuItemsOut], status_code=HTTP_200_OK)
async def read_restaurant_menu_items(db: AsyncSession = Depends(get_db)):
    return await get_restaurant_items(db)


@router.post('/restaurant-menu-items', response_model=RestaurantMenuItemsOut, status_code=HTTP_201_CREATED)
async def create_new_restaurant_menu_item(
        restaurant_menu_item_in: RestaurantMenuItemsIn,
        db: AsyncSession = Depends(get_db),
):
    return await create_restaurant_menu_item(db, restaurant_menu_item_in)


@router.delete('/restaurant-menu-items', status_code=HTTP_204_NO_CONTENT)
async def delete_exist_restaurant_menu_item(restaurant_menu_item_id: int, db: AsyncSession = Depends(get_db)):
    await delete_restaurant_menu_item(db, restaurant_menu_item_id)


@router.patch('/restaurant-menu-items/{restaurant_menu_item_id}', status_code=HTTP_200_OK)
async def update_exist_restaurant_menu_item(
        restaurant_menu_item_id: int,
        restaurant_menu_item_update: RestaurantMenuItemUpdate,
        db: AsyncSession = Depends(get_db),
) -> RestaurantMenuItemsOut:
    restaurant_menu_item_obj = await update_restaurant_menu_item(
        db,
        restaurant_menu_item_update,
        restaurant_menu_item_id,
    )
    return restaurant_menu_item_obj
