#encoding: utf-8
__author__ = 'gpzim98'

from django.db import models
from empresas.models import Empresa

class ContaCaixa(models.Model):
    descricao = models.CharField(max_length=500, null=False, blank=False)
    conta_caixa_superior = models.ForeignKey('self', null=True, blank=True)
    empresa = models.ForeignKey(Empresa)

    class Meta:
        app_label = 'financeiro'
        ordering = ['descricao']

    def __unicode__(self):
        return self.descricao[:20:]