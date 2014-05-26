__author__ = 'gpzim98'
from django import forms
from models import Imovel, ContratoLocacao
from django.forms import ModelForm
from imoveis.models import ContratoAdministrativo


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        exclude = ['endereco']

class ContratoLocacaoForm(forms.ModelForm):
    class Meta:
        model = ContratoLocacao
        exclude = ['data_emissao_contrato']

class ContratoAdministrativoForm(ModelForm):
    class Meta:
        model = ContratoAdministrativo
        fields = ['imovel', 'inicio_contrato', 'termino_contrato',  'empresa']