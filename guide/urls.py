from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from guide.views import *

urlpatterns = [
    path('', WineList),
    path("wine_listing/", WineListing.as_view(), name = 'listing'),
    path("ajax/countries/", getCountries, name = 'get_countries'),
    path("ajax/province/", getProvince, name = 'get_provinces'),
	path("ajax/region/", getRegion, name = 'get_regions'),
]