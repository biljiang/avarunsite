from django.conf.urls import url

from . import views

app_name = 'stocksdemo'
urlpatterns = [
    url(r'^$', views.StocksIndexView.as_view(), name='index'),
    url(r'SP500/', views.SPIndexView.as_view(), name='SP'),
#    url(r'redirect', views.redirect, name='redirect'),
]
