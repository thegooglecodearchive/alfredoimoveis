__author__ = 'gpzim98'
from django import forms
from models import Imovel

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        exclude = ['endereco']

