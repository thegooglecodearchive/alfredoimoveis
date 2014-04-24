from django import forms
from models import ParametrosGerais

class ClasseParametrosGerais(forms.ModelForm):
    class Meta:
        model = ParametrosGerais