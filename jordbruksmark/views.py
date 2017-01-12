# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

from jordbruksmark.models import *


@permission_required('jordbruksmark.is_gardener')
def week_plan_cultivation_list(request, week):
    sets = Satz.objects.filter(anzucht=week)
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
    return render(request, "week_plan_sowing_list.html", renderdict)

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
    return render(request, "week_plan_sowing.html", renderdict)
    
@permission_required('jordbruksmark.is_gardener')
def start(request):
    return redirect('/acker/sets')
    
@permission_required('jordbruksmark.is_gardener')
def sets(request):
    sets = Satz.objects.all()
    renderdict = {
        'sets': sets,
    }
    return render(request, "sets.html", renderdict)
    
@permission_required('jordbruksmark.is_gardener')
def weeks(request):
    cultures = Kultur.objects.all()
    print cultures
    header=["Kultur"]
    for week in range(1, 53):
        header.append(week)
    data=[]    
    for culture in cultures:
	 line={
             'name': culture.name,
             'values': []
         }
         for week in range(1, 53):
              week_value = next(iter(WochenMenge.objects.filter(kultur=culture).filter(woche=week) or []), None)
              line['values'].append({
                  'id':str(week)+"."+str(culture.id),
                  'value': "" if week_value is None else week_value.menge
              })
         data.append(line) 
    
    renderdict = {
        'header': header,
        'data': data,
    }
    return render(request, "weeks.html", renderdict)

@permission_required('jordbruksmark.is_gardener')
def update_weeks(request, id, value):
    ids=id.split('.')
    week=ids[0]
    cultureid=ids[1]
    week_value = next(iter(WochenMenge.objects.filter(kultur__id=cultureid).filter(woche=week) or []), None)
    if week_value is None:
        culture = Kultur.objects.filter(id=cultureid)[0]
        week_value = WochenMenge.objects.create(kultur=culture, woche=week, menge=value);
    else:
        week_value.menge=value
        week_value.save()   
    return HttpResponse(' ')

    
