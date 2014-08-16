from django import forms
from models import ParametrosGerais


class FormParametrosGerais(forms.ModelForm):
    class Meta:
        model = ParametrosGerais
