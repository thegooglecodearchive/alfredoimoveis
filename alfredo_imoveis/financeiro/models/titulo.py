#encoding: utf-8
__author__ = 'gpzim98'

from django.db import models
from empresas.models import Empresa
from financeiro.models.conta_caixa import ContaCaixa
from django.contrib.auth.admin import User
from clientes.models import Cliente
from imoveis.models import ContratoLocacao

TIPO_CONTA = (
    ('D', 'DESPESA'),
    ('R', 'RECEITA'),
)

class Titulo(models.Model):
    descricao = models.CharField(max_length=500, null=False, blank=False)
    conta_caixa = models.ForeignKey(ContaCaixa, null=True, blank=True)
    empresa = models.ForeignKey(Empresa)
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now_add=True)
    vencimento = models.DateField(verbose_name='Data de vencimento')
    data_quitacao = models.DateField(verbose_name='Data de quitação do título', null=True, blank=True)
    tipo = models.CharField(choices=TIPO_CONTA, max_length=1, verbose_name='Tipo da movimentação',
                            help_text='Informe o tipo da movimentação')
    usuario_cadastrou = models.ForeignKey(User, help_text='Não se preocupe, este campo será inserido automáticamente')
    valor = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor do título')
    valor_copasa = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor da COPASA no mês', default=0,null=True,blank=True)
    valor_cemig = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor da CEMIG no mês', default=0,null=True,blank=True)
    valor_outros = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor para outros gastos', default=0,null=True,blank=True)
    perc_juros = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, null=True, blank=True)
    perc_multa = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, null=True, blank=True)
    pagamento_parcial = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor pago até o momento',
                                            null=True, blank=True, default=0)
    deletado = models.NullBooleanField(null=True, blank=True, default=False)
    cliente = models.ForeignKey(Cliente, null=True)
    contrato_locacao = models.ForeignKey(ContratoLocacao, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos'
        ordering =['descricao']

    def __unicode__(self):
        return self.descricao[:20:]+' '+self.vencimento.strftime('%d/%m/%y')\
               +' '+str(self.pagamento_parcial)+'/'+str(self.valor)+' '+self.tipo

class Recibo(models.Model):
    titulo = models.ForeignKey(Titulo)
    data_cadastro = models.DateTimeField(auto_now=True,auto_now_add=True)
    usuario = models.ForeignKey(User)
    descricao = models.TextField()

    def __unicode__(self):
        return u'Título:' + self.titulo.descricao + u' Usuário que emitiu:' + self.usuario.username + u' na data:' + self.data_cadastro.strftime( '%m/%d/%y %H:%M:%S')
    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Recibo'
        verbose_name_plural = 'Recibos'        