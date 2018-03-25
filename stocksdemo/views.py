from django.shortcuts import render
from avarunsite.forms import LoginForm
from django.views.generic import TemplateView
from avarunsite.views import HomePageView
# Create your views here.
from django.http import HttpResponse ,HttpResponseRedirect
import urllib3


class StocksIndexView(HomePageView):
    template_name="stocksdemo/index.html"

class SPIndexView(HomePageView):
    template_name="stocksdemo/SP500.html"




### -----unused old functions ----------------------
Prefix="http://www.avarun.cn:3838/"  
#http = urllib3.PoolManager()
http = urllib3.proxy_from_url("http://www.avarun.com/stocksdemo")
  
def proxy_api(request):  
    url = request.get_full_path()  
    url = Prefix+url  
  
    req = http.request("GET",url)  

    info = req.info()  
    data = req.data  
    return HttpResponse(data, content_type=info.get("content-type"))

def redirect(request):
    return HttpResponseRedirect("http://www.avarun.cn:3838/")

### end unused functions
