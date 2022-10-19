from fastapi import FastAPI
from sqladmin import Admin, ModelView

from backend.config.settings import settings
from backend.db.db_init import engine
from backend.foodcart.api.routers import api_router
from backend.foodcart.models.banners import Banner

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

admin = Admin(app, engine)


class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title]


app.include_router(api_router, prefix=settings.API_V1_STR)

admin.add_view(BannerAdmin)
