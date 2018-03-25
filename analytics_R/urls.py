#from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.conf.urls import url,include
from . import views

app_name = 'analytics_R'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^data_management/', views.DataManagementView.as_view(), name='data_management'),
    url(r'^data_transformation/', views.DataTransformationView.as_view(), name='data_transformation'),
    url(r'^group_summaries/', views.GroupSummariesView.as_view(), name='group_summaries'),
    url(r'^tidy_data/', views.TidyDataView.as_view(), name='tidy_data'),
    url(r'^visualization/', views.VisualizationView.as_view(), name='visualization'),
    url(r'^maps/', views.MapsView.as_view(), name='maps'),
    url(r'^interactive_maps/', views.InteractiveMapsView.as_view(), name='interactive_maps'),
    url(r'^linear_models/', views.LinearModelsView.as_view(), name='linear_models'),
    url(r'^logit_models/', views.LogitModelsView.as_view(), name='logit_models'),
    url(r'^text_intro/', views.TextIntroView.as_view(), name='text_intro'),
    url(r'^corpus_summary/', views.CorpusSummaryView.as_view(), name='corpus_summary'),
#    url(r'^', include('django.contrib.auth.urls')),
]
