from ninja import Router

from foco.views import router as foco_router

app_name = "foco"

foco = Router()
foco.add_router("", foco_router)

urlpatterns = []
