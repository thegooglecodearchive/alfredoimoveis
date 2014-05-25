from django.conf.urls import patterns, include, url
from django.contrib import admin

from enderecos.views import CidadeList, CidadeCreate, CidadeUpdate, CidadeDelete, BairroDelete

urlpatterns = patterns('enderecos.views',
    url(r'^bairro_home/$', 'bairro_home', name='app_enderecos_bairro_home'),
    url(r'^bairro_detalhe/(?P<id>\d+)/$', 'bairro_detalhe', name='app_enderecos_bairro_detalhe'),
    url(r'^bairro_adiciona/$', 'bairro_adiciona', name='app_enderecos_bairro_add'),
    url(r'^bairro_delete(?P<pk>\d+)/$', BairroDelete.as_view(), name='app_enderecos_bairro_delete'),
    url(r'^bairro_update(?P<id>\d+)/$', 'bairro_update', name='app_enderecos_bairro_update'),

    url(r'^cidade_home/$', CidadeList.as_view(), name='app_enderecos_cidade_home'),
    url(r'^cidade_adiciona/$', CidadeCreate.as_view(), name='app_enderecos_cidade_add'),
    url(r'^cidade_editar/(?P<pk>\d+)$', CidadeUpdate.as_view(), name='app_enderecos_cidade_update'),
    url(r'^cidade_delete/(?P<pk>\d+)$', CidadeDelete.as_view(), name='app_enderecos_cidade_delete'),
)
