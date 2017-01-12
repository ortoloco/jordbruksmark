"""jordbruksmark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from jordbruksmark import views as jbm_views
from django.contrib.auth import views as auth_views

urls = [
    url(r'^wp_cultivation/(?P<week>.*?)/', jbm_views.week_plan_cultivation_list),
    url(r'^wp_plant/(?P<week>.*?)/', jbm_views.week_plan_plant_list),
    url(r'^wp_sowing/(?P<week>.*?)/', jbm_views.week_plan_sowing_list),
    url(r'^wp_cultivation$', jbm_views.week_plan_cultivation),
    url(r'^wp_plant$', jbm_views.week_plan_plant),
    url(r'^wp_sowing$', jbm_views.week_plan_sowing),
    url(r'^sets$', jbm_views.sets),
    url(r'^weeks$', jbm_views.weeks),
    url(r'^updateweek/(?P<id>.*?)/(?P<value>.*?)/', jbm_views.update_weeks),
    url(r'^$', jbm_views.sets),
]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$', jbm_views.start),
    url(r'^acker/', include(urls)),    
]
