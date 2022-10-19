from fastapi import FastAPI
from sqladmin import Admin

from backend.admin.admin import BannerAdmin
from backend.config.settings import settings
from backend.db.db_init import engine
from backend.foodcart.api.routers import api_router

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(api_router, prefix=settings.API_V1_STR)

admin = Admin(app, engine)
admin.add_view(BannerAdmin)
