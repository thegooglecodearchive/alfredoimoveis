# encoding:utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'financeiro.views.caixa',
    url(r'^$', 'home', name='app_financeiro_caixa'),
    url(r'^filtra_titulos/$', 'filtra_titulos',
        name='app_financeiro_caixa_filtra_titulos'),
)
