# encoding: utf8
from django.db import models
from enderecos.models import Endereco
from clientes.models import Cliente
from empresas.models import Empresa

# Create your models here.
class Imovel(models.Model):
    descricao = models.CharField(u'Imóvel', max_length=120)
    endereco = models.ForeignKey(Endereco, null = False, blank = False, verbose_name='Endereço')
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

