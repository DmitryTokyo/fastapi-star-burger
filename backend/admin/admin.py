from sqladmin import ModelView

from backend.foodcart.models.banners import Banner


class BannerAdmin(ModelView, model=Banner):  # type: ignore
    column_list = [Banner.id, Banner.title]
