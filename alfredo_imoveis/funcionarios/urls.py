# encoding:utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('funcionarios.views',
    url(r'^$', 'home', name='app_funcionarios_home'),
    url(r'^funcionario_adiciona/$', 'adiciona', name='app_funcionario_add'),
    url(r'^delete(?P<id>\d+)/$', 'delete', name='app_funcionario_delete'),
    url(r'^detalhe(?P<id>\d+)/$', 'detalhe', name='app_funcionario_detalhe'),
    url(r'^update(?P<id>\d+)/$', 'update', name='app_funcionario_update'),

)
