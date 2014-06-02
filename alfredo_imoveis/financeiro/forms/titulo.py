# encoding:utf:8
__author__ = 'gpzim98'
from django import forms
from financeiro.models.titulo import Titulo

#Read only somente após editar uma vez MUITO BOM
def _get_cleaner(form, field):
    def clean_field():
         return getattr(form.instance, field, None)
    return clean_field

class ROFormMixin(forms.BaseForm):
    def __init__(self, *args, **kwargs):
        super(ROFormMixin, self).__init__(*args, **kwargs)
        if hasattr(self, "read_only"):
            if self.instance and self.instance.pk:
                for field in self.read_only:
                    self.fields[field].widget.attrs['readonly'] = "readonly"
                    setattr(self, "clean_" + field, _get_cleaner(self, field))
#---------------------------------------------------------------------
class TituloForm(forms.ModelForm, ROFormMixin):
    read_only = ('valor', 'descricao', 'pagamento_parcial') #Fica habilitado apenas na primeira edição

    class Meta:
        model = Titulo
        exclude = ['usuario_cadastrou', 'deletado', 'juros', 'multa']

