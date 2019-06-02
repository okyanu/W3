from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, HttpResponse, Http404
# from jobs.models import *
from django.contrib.auth.models import Group , User
from django.http import  HttpResponseRedirect
from django.db.models import Count
# from Account.models import *
# from jobs.models import *
# from upload.models import *
from django.contrib.sitemaps import Sitemap
from django.urls import reverse




def homepage(request):

    d = request.POST.get('day')
    if d!=None:
        d = d.split("-")
        y = d[0]
        m = d[1]
        d = d[2]


        request.session['y'] = y
        request.session['m'] = m
        request.session['d'] = d


    hour = request.POST.get('hour')
    minute = request.POST.get('minute')
    hour2 = request.POST.get('hour2')
    minute2 = request.POST.get('minute2')

    location = request.POST.get('location')
    isHome = request.POST.get('home')
    isOutside = request.POST.get('outside')

    if request.POST.get('submit') == 'save':

        d = request.POST.get('day')
        if d != None:
            d = d.split("-")
            request.session['y'] = d[0]
            request.session['m'] = d[1]
            request.session['d'] = d[2]

        request.session['day'] = request.POST.get('day')
        request.session['hour'] = request.POST.get('hour')
        request.session['minute'] = request.POST.get('minute')
        request.session['day2'] = request.POST.get('hour2')
        request.session['minute2'] = request.POST.get('minute2')
        request.session['location'] = request.POST.get('location')
        request.session['home'] = request.POST.get('home')
        request.session['outside'] = request.POST.get('outside')

        if request.POST.get('home') == 'home':

            return HttpResponseRedirect(reverse('SearchApi:home'))

        if request.POST.get('outside') == 'outside':

            return HttpResponseRedirect(reverse('SearchApi:outside'))

        return render(request, 'index.html')

    if d == None or hour == None or minute == None or hour2 == None or minute2 == None:
        return render(request, 'index.html')

    mintime = hour + ':' + minute
    maxtime = hour2 + ':' + minute2



    return render(request, 'index.html')

def homepageNext(request):
    return render(request, 'indexNext.html')