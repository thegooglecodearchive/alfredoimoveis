from django.conf.urls import patterns, include, url

urlpatterns = patterns('clientes.views',
    url(r'^$', 'home', name='app_clientes_home'),
    url(r'^novo$', 'novo', name='app_clientes_novo'),
    url(r'^relatorios$', 'relatorios', name='app_clientes_relatorios'),
    url(r'^delete/(?P<id>\d+)/$', 'delete', name='app_clientes_delete'),
    url(r'^detalhe/(?P<id>\d+)/$', 'detalhe', name='app_clientes_detalhe'),
    url(r'^salvar/(?P<id>\d+)/$', 'salvar', name='app_clientes_salvar'),
    url(r'^filtrar/$', 'filtrar', name='app_clientes_filtrar'),
    url(r'^relatorio/$', 'relatorio', name='app_clientes_relatorio'),
    url(r'^tabela/$', 'tabela', name='app_clientes_tabela'),
)
