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
    
    url(r'^cartas_aniversario_home/$', 'cartas_aniversario_home', name='app_clientes_cartas_aniversario_home'),
    url(r'^cartas_aniversario_individual/(?P<id>\d+)/$', 'cartas_aniversario_individual', name='app_clientes_cartas_aniversario_individual'),
    url(r'^cartas_aniversario_filtrar/$', 'cartas_aniversario_filtrar', name='app_clientes_cartas_aniversario_filtrar'),
)
