from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "File"


urlpatterns = [
    path('upload/', views.Upload, name="Upload"),
    path('show/', views.show_upload, name='Show'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)