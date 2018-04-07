#from django.conf.urls import url

from django.conf.urls import url,include
from . import views

app_name = 'modeling'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='linear_optimization'),
    url(r'^simulation/', views.SimulationView.as_view(), name='simulation'),
    url(r'^prediction/', views.PredictionView.as_view(), name='prediction'),
    url(r'^group_summaries/', views.GroupSummariesView.as_view(), name='group_summaries'),
    url(r'^others/', views.OthersView.as_view(), name='others'),
#    url(r'^', include('django.contrib.auth.urls')),
]
