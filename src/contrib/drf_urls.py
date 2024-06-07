from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apis import DoctorViewSet


router = DefaultRouter()
router.register('doctors', DoctorViewSet, basename='doctors')

urlpatterns = [
    # apis
    path('doctor/', include(router.urls)),

]

