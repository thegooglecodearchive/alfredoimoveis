# encoding:utf-8
from django.db import models
from enderecos.models import Endereco, Cidade
from empresas.models import Empresa

TIPO_CLIENTES = (
    ('C', 'CLIENTE'),
    ('F', 'FIADOR'),
)

ESTATO_CIVIL = (
    ('S', 'SOLTEIRO'),
    ('C', 'CASADO'),
    ('D', 'DIVORCIADO'),
    ('A', 'AMAZIADO'),
)

class Cliente(models.Model):
    nome = models.CharField(max_length = 150, null = False, blank = False)
    cnpj_cpf = models.CharField(max_length = 20,  null = True,  blank = True )
    rg = models.CharField(max_length = 11,  null = True,  blank = True)
    orgao_expeditor = models.CharField(max_length = 5,  null = True,  blank = True, verbose_name=u'Órgão expeditor')
    nome_pai = models.CharField(max_length = 100,  null = True,  blank = True, verbose_name=u'Nome do pai' )
    nome_mae = models.CharField(max_length = 100,  null = True,  blank = True, verbose_name=u'Nome da mãe' )
    nacionalidade = models.CharField(max_length = 50,  null = True,  blank = True, verbose_name=u'Nacionalidade' )
    naturalidade = models.ForeignKey(Cidade, verbose_name=u'Naturalidade', null=True, blank=True)
    endereco = models.ForeignKey(Endereco, null = False, blank = False, related_name = 'endereco_cli')
    empresa = models.ForeignKey(Empresa,  null = True, blank = True)
    ativo = models.NullBooleanField(null = True,             blank = True )
    data_cadastro= models.DateField(auto_now_add = True, null = True, blank = True)
    data_nascimento= models.DateField(null = True, blank = True, verbose_name=u'Data de nascimento')
    telefone_fixo = models.CharField(max_length = 11,  null = True,  blank = True, 
                                verbose_name = 'Telefone Fixo')
    telefone2 = models.CharField(max_length = 11,  null = True,  blank = False, 
                                verbose_name = 'Telefone Fixo')
    telefone_comercial = models.CharField(max_length = 11,  null = True,  blank = True, 
                                 verbose_name = 'Telefone Comercial')
    celular = models.CharField(max_length = 11,  null = True,  blank = True, 
                                 verbose_name = 'Celular')
    celular_2 = models.CharField(max_length = 11,  null = True,  blank = True, 
                                 verbose_name = 'Celular 2')
    email = models.EmailField(null=True, blank=True)
    tipo_cliente = models.CharField(max_length=1, choices=TIPO_CLIENTES, default = 'C',
                                            verbose_name = u'Tipo')
    estado_civil = models.CharField(max_length=1, choices=ESTATO_CIVIL, default = 'S',
                                            verbose_name = u'Estado civíl')
    profissao = models.CharField(max_length = 50,  null = True,  blank = True, verbose_name=u'Profissão' )
    empresa_trabalha = models.CharField(max_length = 50,  null = True,  blank = True, verbose_name=u'Empresa onde trabalha' )
    renda = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u'Renda mensal', default=0)
    socio_empresa = models.BooleanField(default=False, verbose_name=u'É sócio em alguma empresa')
    empresa_socio = models.CharField(max_length = 50,  null = True,  blank = True, verbose_name=u'Empresa na qual é sócio' ,
        help_text=u'Nome da empresa em que é sócio')
    end_empresa_socio = models.CharField(max_length = 50,  null = True,  blank = True, verbose_name=u'Endereço da empresa onde é sócio' ,
        help_text='Endereço da empresa em que é sócio')
    conjuge = models.ForeignKey('self', verbose_name=u'Cônjuge', null=True,blank=True)
    referencias_bancarias = models.TextField(null=True, blank=True, verbose_name=u'Referências bancárias')
    referencias_comerciais = models.TextField(null=True, blank=True, verbose_name=u'Referências comerciais')
    observacoes = models.TextField(null=True, blank=True, verbose_name=u'Observações')
    
    def __unicode__(self):
        return "Cod: " + str(self.id) + " - " +  self.nome