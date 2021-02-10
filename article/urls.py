from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.Post_Article_Show_search, name='post_search'),
    path('article/', views.Post_Article_Show_search, name='postarticle'),
    path('article/post/<int:id>/', views.Post_detail, name='post_detail'),
    path('<int:id>/share/',
         views.post_share, name='post_share'),
]
