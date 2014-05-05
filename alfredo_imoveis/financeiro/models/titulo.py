#encoding: utf-8
__author__ = 'gpzim98'

from django.db import models
from empresas.models import Empresa
from financeiro.models.conta_caixa import ContaCaixa
from django.contrib.auth.admin import User
from clientes.models import Cliente

TIPO_CONTA = (
    ('R', 'RECEITA'),
    ('D', 'DESPESA'),
)

class Titulo(models.Model):
    descricao = models.CharField(max_length=500, null=False, blank=False)
    conta_caixa = models.ForeignKey(ContaCaixa, null=True, blank=True)
    empresa = models.ForeignKey(Empresa)
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now_add=True)
    vencimento = models.DateField(verbose_name='Data de vencimento')
    tipo = models.CharField(choices=TIPO_CONTA, max_length=1, verbose_name='Tipo da movimentação',
                            help_text='Informe o tipo da movimentação')
    usuario_cadastrou = models.ForeignKey(User, help_text='Não se preocupe, este campo será inserido automáticamente')
    valor = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor do título')
    pagamento_parcial = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor pago até o momento',
                                            null=True, blank=True, default=0)
    deletado = models.NullBooleanField(null=True, blank=True, default=False)
    cliente = models.ForeignKey(Cliente, null=True)

    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos'

    def __unicode__(self):
        return self.descricao[:20:]+' '+self.vencimento.strftime('%d/%m/%y')\
               +' '+str(self.pagamento_parcial)+'/'+str(self.valor)+' '+self.tipo