from django.conf.urls import url
from . import views as core_views


app_name = 'Ragister'
urlpatterns = [
    url(r'^account_activation_sent/$', core_views.signup, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
]