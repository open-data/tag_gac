"""tag_gac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.shortcuts import redirect
from guide.views import ajax_type, ajax_code

urlpatterns = [
    path('tag/admin/doc/', include('django.contrib.admindocs.urls')),
    path('tag/admin/', admin.site.urls),
    path('ajax/type/', ajax_type, name = 'ajax_type'),
	path('ajax/code/', ajax_code, name = 'ajax_code'),
    url(r"tag/", include(("guide.urls", "guide"), namespace = "guide")),
    url('^.*$', lambda request: redirect('/tag/0/', permanent=True))
]
