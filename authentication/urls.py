from django.urls import path

from . import views

app_name = 'authentication'


urlpatterns = [
    path('home/', views.mat, name='mat'),
    path('register/', views.index, name='index'),
]