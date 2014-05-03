# encoding: utf8
from django.db import models
from django.contrib.auth.admin import User
from enderecos.models import Endereco
from empresas.models import Empresa

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField('Nome do funcionário', max_length=100)
    rg = models.CharField('Identidade', max_length=20)
    cpf = models.CharField('cpf', max_length=11)
    pis = models.CharField('PIS', max_length=11)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('email', max_length=100)
    cargo = models.CharField('Cargo', max_length=20)
    endereco = models.ForeignKey(Endereco)
    empresa = models.ForeignKey(Empresa)
    data_entrada = models.DateField(auto_now=True,auto_now_add=True)
    data_saida = models.DateField(null=True, blank=True)
    usuario = models.OneToOneField(User)

    def __unicode__(self):
        return self.nome

def retorna_empresa_funcionario(funcionario):
    import pdb;pdb.set_trace()
    return Empresa.objects.filter(id=Funcionario.objects.get(id=funcionario.id).empresa.id)
