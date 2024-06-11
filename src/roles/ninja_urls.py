from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apis import RolesViewSet


router = DefaultRouter()
router.register('', RolesViewSet, basename='Roles')

urlpatterns = [
    path('', include(router.urls)),
    ]