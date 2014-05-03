from django.conf.urls import patterns, include, url

urlpatterns = patterns('imoveis.views',
    url(r'^$', 'home', name='app_imoveis_home'),
    url(r'^adiciona$', 'adiciona', name='app_imoveis_add'),
    url(r'^filtrar/$', 'filtrar', name='app_imoveis_filtrar'),
    url(r'^detalhe/(?P<id>\d+)/$', 'detalhe', name='app_imoveis_detalhe'),
    url(r'^salvar/(?P<id>\d+)/$', 'salvar', name='app_imoveis_salvar'),
    url(r'^delete/(?P<id>\d+)/$', 'delete', name='app_imoveis_delete'),
    url(r'^ficha/(?P<id>\d+)/$', 'ficha', name='app_imoveis_ficha'),
)
