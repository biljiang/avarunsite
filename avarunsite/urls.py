"""avarunsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
#    url(r'^$',views.root_index, name = "root_index" ),
    url(r'^$',views.HomePageView.as_view(), name = "root_index" ),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^analytics_R/', include('analytics_R.urls')),
    url(r'^analytics_P/', include('analytics_P.urls')),
    url(r'^modeling/', include('modeling.urls')),
    url(r'polls/', include('polls.urls')),
    url(r'^stocksdemo/', include('stocksdemo.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/logout/', views.logout_view, name ="logout_view"),
    url(r'^accounts/login/', views.login_view, name ="login_view"),
    url(r'^in_progress/', views.InprogressView.as_view(), name ="inprogress_view"),
]
