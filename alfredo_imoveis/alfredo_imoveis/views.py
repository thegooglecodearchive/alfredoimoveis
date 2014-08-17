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
        configura_sessao(request)
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
    busca_configuracoes(request,dados)
    return render(request, template_dashboard, dados)


def home_barra(request):
    return redirect('/')


def busca_configuracoes(request,dados = {}):
    parametros = ParametrosGerais.objects.all()[0]
    dados['parametros'] = parametros
    dados['nome_empresa'] = request.session['nome_empresa']
    return dados


def configura_sessao(request):
    if request.user.is_authenticated():
        funcionario = Funcionario.objects.filter(usuario=request.user)
        request.session['nome_empresa'] =  funcionario[0].empresa.nome if funcionario else  'Empresa não definida'
    else:
        request.session['nome_empresa'] = 'Empresa não definida'