# encoding: utf8
from django.db import models
from enderecos.models import Endereco
from clientes.models import Cliente
from empresas.models import Empresa

TIPO_CONTRATO = (
    ('R', 'RESIDENCIAL'),
    ('C', 'COMERCIAL')
)

# Create your models here.
class Imovel(models.Model):
    endereco = models.ForeignKey(Endereco, null = False, blank = False, verbose_name='Endereço')
    descricao = models.CharField(u'Imóvel', max_length=120)
    valor_iptu = models.DecimalField('Valor do IPTU',max_digits=6, decimal_places=2)
    valor_aluguel = models.DecimalField('Valor do Aluguel',max_digits=6, decimal_places=2)
    ultima_vistoria = models.DateField(u'Data da última vistoria')
    data_cadastro = models.DateField(auto_now_add=True)
    proprietario = models.ForeignKey(Cliente,verbose_name='Proprietário')
    empresa = models.ForeignKey(Empresa,verbose_name='Filial responsável')
    ativo = models.BooleanField(default=True, verbose_name='Imóvel ativo')

    def __unicode__(self):
        return self.descricao + '-' + self.endereco.rua + '-' + self.proprietario.nome

    @property
    def disponivel(self):
        pass

class ContratoLocacao(models.Model):
    imovel = models.OneToOneField(Imovel)
    inicio_contrato = models.DateField(u'Data do início do contrato')
    termino_contrato = models.DateField(u'Data do término do contrato')
    data_emissao_contrato = models.DateField(auto_now_add=True)
    locatario = models.ForeignKey(Cliente, related_name='locatario_contrato')
    fiador1 = models.ForeignKey(Cliente, related_name='fiador1_contrato')
    fiador2 = models.ForeignKey(Cliente, null=True, blank=True, related_name='fiador2_contrato')
    fiador3 = models.ForeignKey(Cliente, null=True, blank=True, related_name='fiador3_contrato')
    empresa = models.ForeignKey(Empresa,verbose_name='Filial responsável')
    tipo_contrato = models.CharField(max_length=1, choices=TIPO_CONTRATO, verbose_name='Tipo do contrato')
    gerou_receber = models.BooleanField(verbose_name='Já gerou contas a receber', default=False, editable=False)

    def __unicode__(self):
        return self.imovel.descricao[:15:]+ ' - ' +self.locatario.nome
