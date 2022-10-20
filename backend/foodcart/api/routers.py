from fastapi import APIRouter

from backend.foodcart.api.endpoints import banners
from backend.foodcart.api.endpoints import restaurants
from backend.foodcart.api.endpoints import products

api_router = APIRouter()

api_router.include_router(banners.router, prefix='/banners', tags=['banners'])
api_router.include_router(restaurants.router, prefix='/restaurants', tags=['restaurants'])
api_router.include_router(products.router, prefix='/products', tags=['products'])
