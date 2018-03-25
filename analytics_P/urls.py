#from django.conf.urls import url

from django.conf.urls import url,include
from . import views

app_name = 'analytics_P'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^data_management/', views.DataManagementView.as_view(), name='data_management'),
    url(r'^data_transformtion/', views.DataTransformationView.as_view(), name='data_transformation'),
    url(r'^group_summaries/', views.GroupSummariesView.as_view(), name='group_summaries'),
    url(r'^tidy_data/', views.TidyDataView.as_view(), name='tidy_data'),
#    url(r'^', include('django.contrib.auth.urls')),
]
