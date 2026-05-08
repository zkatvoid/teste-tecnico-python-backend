from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from foco.urls import foco as foco_router

api = NinjaAPI()

api.add_router("", foco_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Registro das rotas da API
    path("", api.urls),
]
