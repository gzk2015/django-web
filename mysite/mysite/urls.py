#!/usr/bin/env python
#--encoding:utf-8--

from django.conf.urls import url,include
from django.contrib import admin
from mysite.views import *


urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$',hello),
    url(r'^search-form', search_form),
    url(r'^search/', search),
#    url(r'^blogs-list/',get_blogs),
]
