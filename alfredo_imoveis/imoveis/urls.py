from django.conf.urls import patterns, include, url

urlpatterns = patterns('imoveis.views',
    url(r'^$', 'home', name='app_imoveis_home'),
    url(r'^adiciona$', 'adiciona', name='app_imoveis_add'),
    url(r'^filtrar/$', 'filtrar', name='app_imoveis_filtrar'),
    url(r'^detalhe/(?P<id>\d+)/$', 'detalhe', name='app_imoveis_detalhe'),
    url(r'^salvar/(?P<id>\d+)/$', 'salvar', name='app_imoveis_salvar'),
    url(r'^delete/(?P<id>\d+)/$', 'delete', name='app_imoveis_delete'),
    url(r'^ficha/(?P<id>\d+)/$', 'ficha', name='app_imoveis_ficha'),
    url(r'^adiciona_imovel_para_usuario/(?P<id_cliente>\d+)/$', 'adiciona_imovel_para_usuario', name='app_imoveis_add_imovel_usuario'),

    url(r'^contrato_home/$', 'contrato_home', name='app_imoveis_contrato_home'),
    url(r'^contrato_adicionar/$', 'contrato_adiciona', name='app_imoveis_contrato_add'),
    url(r'^contrato_detalhe/(?P<id>\d+)/$', 'contrato_detalhe', name='app_imoveis_contrato_detalhe'),
    url(r'^contrato_delete/(?P<id>\d+)/$', 'contrato_delete', name='app_imoveis_contrato_delete'),
    url(r'^contrato_salvar/(?P<id>\d+)/$', 'contrato_salvar', name='app_imoveis_contrato_salvar'),
    url(r'^contrato_imprimir/(?P<id>\d+)/$', 'contrato_imprimir', name='app_imoveis_contrato_imprimir'),
    url(r'^contrato_gerar_receber/(?P<id>\d+)/$', 'contrato_gerar_receber', name='app_imoveis_contrato_gerar_receber'),
)


