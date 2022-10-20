from fastapi import APIRouter

from backend.foodcart.api.endpoints import banners
from backend.foodcart.api.endpoints import restaurants

api_router = APIRouter()

api_router.include_router(banners.router, prefix='/banners', tags=['banners'])
api_router.include_router(restaurants.router, prefix='/restaurants', tags=['restaurants'])
