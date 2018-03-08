from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from avarunsite.forms import LoginForm
#@login_required
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#    return HttpResponseRedirect("https://www.avarun.cn/stocksdemo")

def index(request):
    login_form = LoginForm()
    return render(request,"polls/index.html",{"content":"You are in Polls","login_form": login_form})
#
