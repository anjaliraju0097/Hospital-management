from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apis import UserViewSet


router = DefaultRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    ]