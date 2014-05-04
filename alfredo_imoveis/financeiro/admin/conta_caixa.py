from django.contrib import admin
from financeiro.models.conta_caixa import ContaCaixa

# Register your models here.
class ContaCaixaAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContaCaixa, ContaCaixaAdmin)
