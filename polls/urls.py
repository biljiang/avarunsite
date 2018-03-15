#from django.conf.urls import url

from django.conf.urls import url,include
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^', include('django.contrib.auth.urls')),
]
