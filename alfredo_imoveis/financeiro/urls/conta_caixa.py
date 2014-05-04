# encoding:utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('financeiro.views.conta_caixa',
    url(r'^$', 'home', name='app_financeiro_conta_caixa_home'),
    url(r'^detalhe/(?P<id>\d+)/$', 'detalhe', name='app_financeiro_conta_caixa_detalhe'),
    url(r'^adicionar/$', 'adicionar', name='app_financeiro_conta_caixa_add'),
    url(r'^delete/(?P<id>\d+)/$', 'delete', name='app_financeiro_conta_caixa_delete'),
    url(r'^salvar/(?P<id>\d+)/$', 'salvar', name='app_financeiro_conta_caixa_salvar'),
    url(r'^filtrar/$', 'filtrar', name='app_financeiro_conta_caixa_filtrar'),

)
