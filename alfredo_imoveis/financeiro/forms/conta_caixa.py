__author__ = 'gpzim98'
from django import forms
from financeiro.models.conta_caixa import ContaCaixa

class ContaCaixaForm(forms.ModelForm):
    class Meta:
        model = ContaCaixa



