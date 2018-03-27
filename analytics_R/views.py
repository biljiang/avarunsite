from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.http import HttpResponse #,HttpResponseRedirect
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from avarunsite.forms import LoginForm
from avarunsite.views import HomePageView
#@login_required
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#    return HttpResponseRedirect("https://www.avarun.cn/stocksdemo")

class IndexView(HomePageView):
    template_name='analytics_R/index.html'

class DataManagementView(HomePageView):
    template_name='analytics_R/data_management.html'

class DataTransformationView(HomePageView):
    template_name='analytics_R/data_transformations.html'

class GroupSummariesView(HomePageView):
    template_name='analytics_R/group_summaries.html'

class TidyDataView(HomePageView):
    template_name='analytics_R/tidy_data.html'

class VisualizationView(HomePageView):
    template_name='analytics_R/visualization.html'

class MapsView(HomePageView):
    template_name='analytics_R/maps.html'

class InteractiveMapsView(HomePageView):
    template_name='analytics_R/interactive_maps.html'

class LinearModelsView(HomePageView):
    template_name='analytics_R/linear_models.html'

class LogitModelsView(HomePageView):
    template_name='analytics_R/logit_models.html'

# login required from urls.py
class TextIntroView(HomePageView):
    template_name='analytics_R/text_intro.html'

class CorpusSummaryView(HomePageView):
    template_name='analytics_R/corpus_summary.html'

# Mixin View for login_required
class DatabaseAccessView(LoginRequiredMixin,HomePageView):
    template_name='analytics_R/in_progress.html'
    login_url = '/login/'
#    redirect_field_name = 'redirect_to'


# bug found if name="as_view"
@method_decorator(login_required, name='dispatch')
class KmeansView(HomePageView):
    template_name='analytics_R/in_progress.html'


# login required from urls.py
class ClassificationView(HomePageView):
    template_name='analytics_R/in_progress.html'
    

@method_decorator(login_required, name='dispatch')
class SentimentView(RedirectView):
    url="/stocks_reactive/"


