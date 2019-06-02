
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import outside,home


app_name = 'SearchApi'

urlpatterns = [

    # url(r'^sitemap\.xml/$', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
    url(r'^outside/$', outside , name='outside'),
    url(r'^home/$', home, name='home'),

]