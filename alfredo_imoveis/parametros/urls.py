# encoding:utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'parametros.views',
    url(r'^$', 'home', name='app_parametros_home'),
    url(r'^editar/(?P<id>\d+)/$', 'editar', name='app_parametros_editar'),
    url(r'^salvar/(?P<id>\d+)/$', 'salvar', name='app_parametros_salvar'),
)
