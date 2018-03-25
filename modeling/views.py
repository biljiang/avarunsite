from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from avarunsite.forms import LoginForm
from avarunsite.views import HomePageView
#@login_required
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#    return HttpResponseRedirect("https://www.avarun.cn/stocksdemo")

class IndexView(HomePageView):
    template_name='modeling/index.html'

class DataManagementView(HomePageView):
    template_name='modeling/data_management.html'

class DataTransformationView(HomePageView):
    template_name='modeling/data_transformations.html'

class GroupSummariesView(HomePageView):
    template_name='modeling/group_summaries.html'

class TidyDataView(HomePageView):
    template_name='modeling/tidy_data.html'


