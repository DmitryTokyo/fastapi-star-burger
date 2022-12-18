from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_200_OK

from backend.db.db_deps import get_db
from backend.foodcart.schemas.restaurants import (
    RestaurantOut, RestaurantIn, RestaurantMenuItemsOut, RestaurantMenuItemsIn, RestaurantUpdate,
    RestaurantMenuItemUpdate,
)

from backend.foodcart.crud.restaurant import crud_restaurant, crud_restaurant_menu_item

router = APIRouter()


@router.get('/', response_model=list[RestaurantOut], status_code=HTTP_200_OK)
async def read_restaurants(db: AsyncSession = Depends(get_db)):
    return await crud_restaurant.get_multi(db)


@router.post('/', response_model=RestaurantOut, status_code=HTTP_201_CREATED)
async def create_new_restaurant(restaurant_in: RestaurantIn, db: AsyncSession = Depends(get_db)):
    return await crud_restaurant.create(db, restaurant_in)


@router.delete('/', status_code=HTTP_204_NO_CONTENT)
async def delete_exist_restaurant(restaurant_id: int, db: AsyncSession = Depends(get_db)) -> dict:
    await crud_restaurant.delete(db, restaurant_id)
    return {'deleted object': restaurant_id}


@router.patch('/{restaurant_id}', response_model=RestaurantOut, status_code=HTTP_200_OK)
async def update_exist_restaurant(
        restaurant_id: int,
        restaurant_update_in: RestaurantUpdate,
        db: AsyncSession = Depends(get_db),
):
    await crud_restaurant.update(db, restaurant_update_in, restaurant_id)
    return crud_restaurant.get_single(db, restaurant_id)


@router.get('/restaurant-menu-items', response_model=list[RestaurantMenuItemsOut], status_code=HTTP_200_OK)
async def read_restaurant_menu_items(db: AsyncSession = Depends(get_db)):
    return await crud_restaurant_menu_item.get_multi(db)


@router.post('/restaurant-menu-items', response_model=RestaurantMenuItemsOut, status_code=HTTP_201_CREATED)
async def create_new_restaurant_menu_item(
        restaurant_menu_item_in: RestaurantMenuItemsIn,
        db: AsyncSession = Depends(get_db),
):
    return await crud_restaurant_menu_item.create(db, restaurant_menu_item_in)


@router.delete('/restaurant-menu-items', status_code=HTTP_204_NO_CONTENT)
async def delete_exist_restaurant_menu_item(restaurant_menu_item_id: int, db: AsyncSession = Depends(get_db)) -> dict:
    await crud_restaurant_menu_item.delete(db, restaurant_menu_item_id)
    return {'deleted object': restaurant_menu_item_id}


@router.patch('/restaurant-menu-items/{restaurant_menu_item_id}', status_code=HTTP_200_OK)
async def update_exist_restaurant_menu_item(
        restaurant_menu_item_id: int,
        restaurant_menu_item_update: RestaurantMenuItemUpdate,
        db: AsyncSession = Depends(get_db),
) -> RestaurantMenuItemsOut:
    await crud_restaurant_menu_item.update(
        db,
        restaurant_menu_item_update,
        restaurant_menu_item_id,
    )

    return await crud_restaurant_menu_item.get_single(db, restaurant_menu_item_id)
