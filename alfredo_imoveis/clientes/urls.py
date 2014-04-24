from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('clientes.views',
    url(r'^$', 'home', name='app_clientes_home'),
)
