from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf/', include('contrib.drf_urls')),
    path('api/ninja/', include('contrib.ninja_urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.USE_SILK:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
