# encoding:utf-8
from django.db import models
from enderecos.models import Endereco
from empresas.models import Empresa

TIPO_CLIENTES = (
    ('C', 'CLIENTE'),
    ('F', 'FIADOR'),
)

class Cliente(models.Model):
    nome = models.CharField(max_length = 150, null = False, blank = False)
    cnpj_cpf = models.CharField(max_length = 20,  null = True,  blank = True )
    rg = models.CharField(max_length = 11,  null = True,  blank = True )
    endereco = models.ForeignKey(Endereco, null = False, blank = False, related_name = 'endereco_cli')
    endereco_cobranca= models.ForeignKey(Endereco, null = True,  blank = True,
                                         related_name = 'endereco_obra', verbose_name = 'Endereço da obra')
    empresa = models.ForeignKey(Empresa,  null = False, blank = False       )
    ativo = models.NullBooleanField(null = True,             blank = True )
    data_cadastro= models.DateField(auto_now_add = True, null = True, blank = True)
    telefone = models.CharField(max_length = 11,  null = False,  blank = False, default = '0',
                                verbose_name = 'Telefone 1')
    telefone2 = models.CharField(max_length = 11,  null = False,  blank = False, default = '0',
                                 verbose_name = 'Telefone 2')
    telefone3 = models.CharField(max_length = 11,  null = False,  blank = False, default = '0',
                                 verbose_name = 'Telefone 3')
    email = models.EmailField(null=True)
    tipo_cliente = models.SmallIntegerField(choices=TIPO_CLIENTES, default = 1,
                                            verbose_name = u'Tipo')

    def __unicode__(self):
        return "Cod: " + str(self.id) + " - " +  self.nome

