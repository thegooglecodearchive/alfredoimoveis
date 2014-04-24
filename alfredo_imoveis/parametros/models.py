# encoding:utf8
from django.db import models
from django.contrib.auth.models import User

class ParametrosGerais(models.Model):
    taxa_juros = models.DecimalField(max_digits=3, decimal_places=1)
    texto_carta_aniv1 = models.TextField('Texto da carta de aniversário 1')
    texto_carta_aniv2 = models.TextField('Texto da carta de aniversário 2')
    texto_carta_aniv3 = models.TextField('Texto da carta de aniversário 3')
    clausula_contrato_adic = models.TextField('Cláusula de contrato adicional')
    gerente = models.ForeignKey(User, verbose_name="Usuário gerente",
                                help_text="Informe o usuário gerente da empresa")