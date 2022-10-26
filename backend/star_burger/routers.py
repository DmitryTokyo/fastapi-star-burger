from fastapi import APIRouter

from backend.star_burger.endpoints import images

router = APIRouter()

router.include_router(images.router, prefix='/images', tags=['images'])