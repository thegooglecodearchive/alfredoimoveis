# encoding:utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('financeiro.views.views_principal',
    url(r'^$', 'home', name='app_financeiro_home'),
    url(r'^conta_caixa/', include('financeiro.urls.conta_caixa')),
    url(r'^titulos/', include('financeiro.urls.titulo')),

)
