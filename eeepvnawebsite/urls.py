from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('informatica/', include('informatica.urls', namespace='informatica')),
    path('', include('base.urls', namespace='base'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
