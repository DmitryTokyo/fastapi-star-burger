from sqladmin import ModelView

from backend.foodcart.models.banners import Banner


class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title]
