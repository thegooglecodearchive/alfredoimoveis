__author__ = 'gpzim98'
from django import forms
from models import Endereco

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
