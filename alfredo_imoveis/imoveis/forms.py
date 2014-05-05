__author__ = 'gpzim98'
from django import forms
from models import Imovel, ContratoLocacao

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        exclude = ['endereco']

class ContratoLocacaoForm(forms.ModelForm):
    class Meta:
        model = ContratoLocacao
        exclude = ['data_emissao_contrato']