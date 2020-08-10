from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('adminDashboard/', admin.site.urls),
    path('admin/', include('app.urls')),
    path('', include('frontend.urls')),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
