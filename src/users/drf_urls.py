# your_app_name/urls.py
from django.urls import path
from ninja import NinjaAPI
from .apis import router as user_router

api = NinjaAPI()
api.add_router("", user_router)

urlpatterns = [
    path("", api.urls),
]
