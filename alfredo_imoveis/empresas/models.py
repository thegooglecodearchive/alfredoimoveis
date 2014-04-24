# encoding:utf-8
from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length = 150, null = False, blank = False)
    ativo = models.NullBooleanField(null = False, blank = False, default=True)

    def __unicode__(self):
        return self.nome
