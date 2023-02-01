"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from mysite.views import *
from mysite.currentTime import *
from books.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',hello),
    re_path(r'^now/(\d{1})/$',currentTime),
    path('tp/',temp),
    path('cod1/',condi1),
    path('cod2/',condi2),
    path('forl/',forloop),
    path('f1/',filter1),
    path('inh/',inh),
    path('rq/',allRequest),
    path('s1/',search_form),
    path('search/',search),
    path('cur/',current_page),
    path('login/',login),
    path('csv1/',mkCSV1),
    path('csv2/',mkCSV2),
    path('ss1/',session1),
    path('ss2/',session2),
]

if settings.DEBUG:
    urlpatterns +=[re_path(r'^debuginfo/$',debug)]