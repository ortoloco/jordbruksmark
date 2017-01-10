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
from django.conf.urls import url
from django.contrib import admin
from jordbruksmark import views as jbm_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^acker/wp_cultivation/(?P<week>.*?)/', jbm_views.week_plan_cultivation_list),
    url(r'^acker/wp_plant/(?P<week>.*?)/', jbm_views.week_plan_plant_list),
    url(r'^acker/wp_sowing/(?P<week>.*?)/', jbm_views.week_plan_sowing_list),
    url(r'^acker/wp_cultivation$', jbm_views.week_plan_cultivation),
    url(r'^acker/wp_plant$', jbm_views.week_plan_plant),
    url(r'^acker/wp_sowing$', jbm_views.week_plan_sowing),
]
