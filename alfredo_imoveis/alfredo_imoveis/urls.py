# encoding:utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('alfredo_imoveis.views',
    url(r'^$', 'home', name='main_home'),

    #Aplicações
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^clientes/', include('clientes.urls')),
    url(r'^parametros/$', include('parametros.urls')),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name':'index.html'}, name = 'url_login'),
    url(r'^accounts/profile/$', 'alfredo_imoveis.views.dashboard',
        name='url_dashboard'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name':'index.html'}, name = 'url_login'),

    url(r'^admin/', include(admin.site.urls)),
)
