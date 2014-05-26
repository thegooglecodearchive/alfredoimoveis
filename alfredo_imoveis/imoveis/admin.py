from django.contrib import admin
from imoveis.models import Imovel, ContratoLocacao, ContratoAdministrativo

# Register your models here.
admin.site.register(Imovel)
admin.site.register(ContratoLocacao)
admin.site.register(ContratoAdministrativo)
