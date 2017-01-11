# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from jordbruksmark.models import *


@permission_required('jordbruksmark.is_gardener')
def week_plan_cultivation_list(request, week):
    print week
    sets = Satz.objects.filter(anzucht=week)
    print sets
    renderdict = {
        'sets': sets,
    }
    return render(request, "week_plan_cultivation_list.html", renderdict)
    
@permission_required('jordbruksmark.is_gardener')
def week_plan_plant_list(request, week):
    sets = Satz.objects.filter(setzen=week)
    renderdict = {
        'sets': sets,
    }
    return render(request, "week_plan_plant_list.html", renderdict)
    
@permission_required('jordbruksmark.is_gardener')
def week_plan_sowing_list(request, week):
    sets = Satz.objects.filter(saat=week)
    renderdict = {
        'sets': sets,
    }
    return render(request, "week_plan_plant_list.html", renderdict)

@permission_required('jordbruksmark.is_gardener')
def week_plan_cultivation(request):
    renderdict ={}
    return render(request, "week_plan_cultivation.html", renderdict)
    
@permission_required('jordbruksmark.is_gardener')
def week_plan_plant(request):
    renderdict ={}
    return render(request, "week_plan_plant.html", renderdict)
    
@permission_required('jordbruksmark.is_gardener')
def week_plan_sowing(request):
    renderdict ={}
    return render(request, "week_plan_plant.html", renderdict)

    
