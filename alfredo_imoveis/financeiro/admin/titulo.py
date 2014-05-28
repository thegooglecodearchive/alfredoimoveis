from django.contrib import admin
from financeiro.models.titulo import Titulo, Recibo

# Register your models here.
class TituloAdmin(admin.ModelAdmin):

    readonly_fields = ['usuario_cadastrou']
    def save_model(self,request, obj, form, change):
        obj.usuario_cadastrou = request.user
        obj.save()
admin.site.register(Titulo, TituloAdmin)
admin.site.register(Recibo)
