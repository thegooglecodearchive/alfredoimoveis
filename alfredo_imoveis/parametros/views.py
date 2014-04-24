# encoding:utf8
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from forms import ClasseParametrosGerais
from models import ParametrosGerais
# Create your views here.

template_parametros = 'parametros/home.html'

@login_required
def home(request):
    dados = {}

    if request.method == 'GET':
        param = ParametrosGerais.objects.get(id=1)
        if param:
            form = ClasseParametrosGerais(instance=param)
        else:
            form = ClasseParametrosGerais()
        dados['form'] = form
        return render(request, template_parametros, dados)
    else:
        form = ClasseParametrosGerais(request.POST or None)
        if form.is_valid():
            param = form.save(commit=False)
            param.save()
            dados['form'] = form
            dados['mensagem'] = 'Parâmetros salvos com sucesso'
            return render(request, template_parametros, dados)