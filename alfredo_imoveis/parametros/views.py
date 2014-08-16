# encoding:utf8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import FormParametrosGerais
from models import ParametrosGerais
# Create your views here.

template_parametros = 'parametros/home.html'


@login_required
def home2(request):
    dados = {}
    if request.method == 'GET':
        param = ParametrosGerais.objects.filter(id=1)
        if param.count() > 0:
            p = param[0]
            form = FormParametrosGerais(instance=p)
        else:
            form = FormParametrosGerais()
            dados['mensagem'] = 'Você ainda não cadastrou parâmetros'
        dados['form'] = form
        return render(request, template_parametros, dados)
    else:
        form = FormParametrosGerais(request.POST or None)
        if form.is_valid():
            param = form.save(commit=False)
            param.id = 1
            param.save()
            dados['form'] = form
            dados['mensagem'] = 'Parâmetros salvos com sucesso'
            return render(request, template_parametros, dados)
        else:
            dados['form'] = form
            dados['mensagem'] = 'Ops, alguns erros foram encontrados.'
            return render(request, template_parametros, dados)


@login_required
def home(request, mensagem=''):
    dados = {}
    param = ParametrosGerais.objects.all()[0]
    form = FormParametrosGerais(instance=param)
    dados['parametro'] = param
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
    dados['form'] = form
    return render(request, template_parametros, dados)


def editar(request, id):
    dados = {}
    param = ParametrosGerais.objects.get(id=id)
    form = FormParametrosGerais(instance=param)
    dados['form'] = form
    dados['modo'] = 'EDICAO'
    dados['parametro'] = param
    return render(request, template_parametros, dados)


def salvar(request, id):
    dados = {}
    form = FormParametrosGerais(request.POST or None)
    if form.is_valid():
        param = form.save(commit=False)
        param.id = id
        param.save()
        dados['mensagem'] = u'Parâmetros salvos com sucesso'
        dados['parametro'] = param
        dados['form'] = form
        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
        return render(request, template_parametros, dados)
    else:
        dados = {}
        dados['form'] = form
