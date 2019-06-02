from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from hackathonBase.views import *
from django.http import HttpResponseRedirect
from pinax.messages.views import InboxView, MessageCreateView ,ThreadView , ThreadDeleteView,InboxView
from django.views.defaults import page_not_found
from django.conf.urls import handler404 , handler500
# from Account import views as myapp_views
from django.shortcuts import render, redirect, HttpResponse, Http404
from registration.backends.default.urls import urlpatterns as other_app_urls
from django.contrib.sitemaps import views
# from django.contrib.sitemaps.views import sitemap, index
from django.views.decorators.cache import cache_page
from .views import homepage






admin.site.site_title = "Hackathon Base"

app_name = 'hackathonBase'

urlpatterns = [
    url(r'^management/administration', admin.site.urls),
    url(r'^$', homepage),
    url(r'^next/$', homepageNext),
    # url(r'^sitemap\.xml/$', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
    url(r'^searchAPI/', include('SearchApi.urls')),



]







urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
