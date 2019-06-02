from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, HttpResponse, Http404
from django.contrib.auth.models import Group , User
from django.http import  HttpResponseRedirect
from django.db.models import Count
from django.urls import reverse
import json
import requests
import urllib.request
import requests
import json
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


def home(request):


    if request.method == 'POST':
        d = request.POST.get('mood')
        if d == None:
            return render(request, 'index.html', {})
        client_credentials_manager = SpotifyClientCredentials(client_id='56dcfbaa55a74346b745e0172971f727',client_secret='01709880429a4d329897ac276cab8575')
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        results = spotify.category_playlists(category_id=d, country='US', limit=10, offset=5)


        counter = 0
        dict = {}
        d = request.session['d']
        y = request.session['y']
        m = request.session['m']
        hour = request.session['hour']
        minute = request.session['minute']
        hour2 = request.session['day2']
        minute2 = request.session['minute2']

        if d == None or y == None or m == None or hour == None or minute == None or hour2 == None or minute2 == None:
            return render(request, 'index.html', {})
        mintime = hour + ':' + minute
        maxtime = hour2 + ':' + minute2

        r = requests.get('http://api.tvmaze.com/schedule?country=US&date=%s-%s-%s' % (y, m, d), auth=('user', 'pass'))
        k = r.json()
        for i in k:
            if mintime < i['airtime'] and i['airtime'] < maxtime:
                if counter < 10:
                    # print('hop')
                    dict[counter]=i
                    # print (i['show']['name'])
                    # print (i['show']['network']['name'])
                    # print (i['airtime'])
                    counter += 1
        dict2 = {}
        if request.method == 'POST':
            counter = 0
            d = request.POST.get('in')

            r = requests.get('http://www.recipepuppy.com/api/?i = %s' % (d), auth=('user', 'pass'))
            k = r.json()
            for i in k['results']:
                if counter < 5:
                    dict2[counter]=i
                counter +=1

        dict3 ={}
        counter = 0
        r = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=2d819f8c91e8446993cfd52d1e63a339&language=en-US&page=1',auth=('user', 'pass'))
        k = r.json()
        for i in k['results']:
            if counter < 5:
               dict3[counter]= i
            counter += 1


        context = {
            'spo': results['playlists']['items'],
            'tv': dict,
            'rec': dict2,
            'film':dict3,
        }

        return render(request,'homeresult.html',context)

    return render(request, 'home.html', {})




oauth = 'Bearer OXE7PISJWN2ZBNT3LWWO'

key = '4f2f78570e227f76794d51a9e8473f4b'

def outside(request):
    location = request.session['location']
    locationQuery = requests.get('https://developers.zomato.com/api/v2.1/locations?query=' + str(location),headers={'user-key': key}).json()
    latitude = locationQuery['location_suggestions'][0]['latitude']
    longitude = locationQuery['location_suggestions'][0]['longitude']
    cuisines = requests.get('https://developers.zomato.com/api/v2.1/cuisines?lat=' + str(latitude) + '&lon=' + str(longitude),headers={'user-key': key}).json()
    establishments = requests.get('https://developers.zomato.com/api/v2.1/establishments?city_id=' + str(locationQuery['location_suggestions'][0]['city_id']), headers={'user-key': key}).json()
    # print(establishments)

    if request.POST.get('submit')=='submit':
        cuisinesX=request.POST.getlist('cuisine')
        categoryX = request.POST.getlist('category')

        cuisineXStr = ''
        categoryStr= ''

        for i in range(len(cuisinesX)):
            if i == (len(cuisinesX)-1):
                cuisineXStr +=cuisinesX[i]
            else:
                cuisineXStr += cuisinesX[i] + '%2C'


        for i in range(len(categoryX)):

            if i == (len(categoryX)-1):
                categoryStr +=categoryX[i]
            else:
                categoryStr += categoryX[i] + '%2C'



        location = request.session['location']
        locationQuery = requests.get('https://developers.zomato.com/api/v2.1/locations?query='+str(location),headers={'user-key': key}).json()
        # entity id , entity-group  city id , ctiy name country id , country name
        # r = request.POST.get()
        latitude = locationQuery['location_suggestions'][0]['latitude']
        longitude = locationQuery['location_suggestions'][0]['longitude']
        entity_id = locationQuery['location_suggestions'][0]['entity_id']
        entity_type = locationQuery['location_suggestions'][0]['entity_type']
        city_id = locationQuery['location_suggestions'][0]['city_id']






        restaurants = requests.get('https://developers.zomato.com/api/v2.1/search?count=20&lat=40.742051&lon=-74.004821&radius=15000&cuisines='+cuisineXStr+'&establishment_type='+categoryStr+'&sort=rating&order=desc',headers={'user-key': key}).json()




        nightlife = requests.get('https://developers.zomato.com/api/v2.1/search?count=20&lat=' + str(locationQuery['location_suggestions'][0]['latitude']) + '&lon=' + str(locationQuery['location_suggestions'][0]['longitude']) + '&radius=15000&establishment_type='+categoryStr+'&category=3&sort=rating&order=desc',headers={'user-key': key}).json()


        #Events


        day = request.session['day']
        # print(locationQuery)
        events = requests.get('https://www.eventbriteapi.com/v3/events/search?location.latitude=' + str(locationQuery['location_suggestions'][0]['latitude']) + '&location.longitude=' + str(locationQuery['location_suggestions'][0]['longitude']) + '&start_date.range_start='+str(day)+'T00%3A00%3A00&start_date.range_end='+str(day)+'T23%3A59%3A59', headers={'Authorization': oauth}).json()



        counter = 0
        # print(events['pagination']['page_count'])

        for i in range(events['pagination']['page_count']):
            if counter < 20:
                pass
                print(events['events'][i]['name'])
            else:
                break
            counter += 1

        context={
            'restaurants': restaurants['restaurants'],
            'events': events,
            'nightlife': nightlife,
        }


    context = {
        'cuisines':cuisines['cuisines'],
        'establishments': establishments['establishments'],
    }

    return render(request, 'outside.html', context)


def Landmarks(request):
    landmarks = requests.get('https://geocoder.api.here.com/6.2/geocode.json?prox=37.43823,-122.17796,1000&mode=retrieveLandmarks&app_id=vShCV8P3oGTOEdvXLiLi&app_code=VQyr3f0t7wrFJLXYT1Uo_Q&city=New%20York&prox=37.7442,-119.5931,1000').json()
    # landmarks = requests.get('http://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.xml?prox=37.43823,-122.17796,1000&mode=retrieveLandmarks&app_id=vShCV8P3oGTOEdvXLiLi&app_code=VQyr3f0t7wrFJLXYT1Uo_Q&gen=9').json()

    print(landmarks)
    return render(request, 'APIs/landmarks.html')

# Create your views here.
