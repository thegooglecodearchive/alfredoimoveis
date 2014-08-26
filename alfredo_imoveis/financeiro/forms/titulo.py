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
                    self.fields[field].widget.attrs['disabled'] = True
                    setattr(self, "clean_" + field, _get_cleaner(self, field))


#---------------------------------------------------------------------
class TituloForm(forms.ModelForm, ROFormMixin):
    #Fica habilitado apenas na primeira edição
    read_only = (
        'valor', 'descricao', 'pagamento_parcial',
        'conta_parcelas', 'cliente', 'tipo', 'vencimento',
        'contrato_locacao', 'conta_caixa', 'empresa')

    class Meta:
        model = Titulo
        exclude = [
            'usuario_cadastrou', 'deletado', 'juros', 'perc_multa',
            'valor_iptu_pago', 'valor_condominio_pago']
