__author__ = 'gpzim98'
from django import forms
from financeiro.models.titulo import Titulo

class TituloForm(forms.ModelForm):
    class Meta:
        model = Titulo
        exclude = ['usuario_cadastrou']
        exclude = ['usuario_cadastrou']



