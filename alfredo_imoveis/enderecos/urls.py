from django.conf.urls import patterns, include, url

from django.contrib import admin

urlpatterns = patterns('enderecos.views',
    url(r'^bairro_home/$', 'bairro_home', name='app_enderecos_bairro_home'),
    url(r'^bairro_detalhe/(?P<id>\d+)/$', 'bairro_detalhe', name='app_enderecos_bairro_detalhe'),
    url(r'^bairro_adiciona/$', 'bairro_adiciona', name='app_enderecos_bairro_add'),
    url(r'^bairro_delete(?P<id>\d+)/$', 'bairro_delete', name='app_enderecos_bairro_delete'),
    url(r'^bairro_update(?P<id>\d+)/$', 'bairro_update', name='app_enderecos_bairro_update'),
)
