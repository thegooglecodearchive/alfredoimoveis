# encoding: utf8
__author__ = 'gpzim98'
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from funcionarios.models import Funcionario
from parametros.models import ParametrosGerais

template_home = 'index.html'
template_dashboard = 'dashboard.html'


def home(request):
    if request.user.is_authenticated():
        return dashboard(request)
    else:
        return redirect('url_login')

@login_required
def dashboard(request):
    dados = {}

    if not Funcionario.objects.filter(usuario=request.user):
        dados['mensagem'] = """Atenção não foi encontrado um funcionário associado a este usuário,
                               isso pode causar sérios problemas no sistema, acesse o cadastro de funcionários
                               e crie um funcionário para este usuário.
                            """
    return render(request, template_dashboard, dados)

def home_barra(request):
    return redirect('/')

def busca_configuracoes(dados = {}):
    parametros = ParametrosGerais.objects.get(id=1)
    dados['parametros'] = parametros
    return dados

    
