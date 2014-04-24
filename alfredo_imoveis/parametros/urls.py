# encoding:utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('parametros.views',
    url(r'^$', 'home', name='app_parametros_home'),
)