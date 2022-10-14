from fastapi import APIRouter

from backend.foodcart.api.endpoints import banners

api_router = APIRouter()
api_router.include_router(banners.router, tags=['banners'])
