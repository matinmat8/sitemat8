from django.urls import path
from . import views

app_name = "File"


urlpatterns = [
    path('upload/', views.Upload, name="Upload")
]