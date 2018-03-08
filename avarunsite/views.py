from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
from django.views.generic import TemplateView
#import urllib3
from django.contrib.auth import authenticate, login, logout


class HomePageView(TemplateView):
    template_name = "site/index.html"
    login_form = LoginForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = self.login_form
        context['content'] = "You are in site HomePage"
        return context


def root_index(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
    """
    else:
        user = None
    """
    login_form = LoginForm()

    return render (request,'site/index.html',{'login_form':login_form,'user':request.user})
#    return HttpResponse("Hello, world. You're at the root index.")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')




#def root_index(request):
#    return HttpResponse("Hello, world. You're at the root index.")


"""
Prefix="http://www.avarun.cn:3838/"  
http = urllib3.PoolManager()
  
def proxy_api(request):  
3def root_index(request):  
    url = request.get_full_path()  
    url = Prefix+url  
  
    req = http.request("GET",url)  

    info = req.info()  
    data = req.data  
    return HttpResponse(data, content_type=info.get("content-type"))
"""


