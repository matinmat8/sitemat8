from django.urls import path
from . import views

app_name = "File"


urlpatterns = [
    path('test/', views.Upload, name="Upload")
]