from django.urls import path
from django.contrib.auth import views as auth_views


from . import views
from django.contrib.auth import views as auth_views

app_name = 'authentication'


urlpatterns = [
    path('register/home/', views.mat, name='mat'),
    path('register/', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/Login.html'))
    #path('reset_password/',
         #auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
         #name='password_reset'),

    #path('reset_password_sent/',
         #auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'),
         #name='password_reset_done'),

    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='reset_password_complete'),
]