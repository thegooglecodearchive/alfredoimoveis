# encoding: utf8
from django.shortcuts import render, get_object_or_404
from financeiro.models.conta_caixa import ContaCaixa
from funcionarios.models import Funcionario
from financeiro.forms.conta_caixa import ContaCaixaForm
from datetime import datetime, date

today = date.today()

template_home = 'financeiro/conta_caixa/home.html'
template_novo = 'financeiro/conta_caixa/novo.html'
template_detalhe = 'financeiro/conta_caixa/detalhe.html'
template_relatorio = 'financeiro/conta_caixa/relatorio.html'
# Create your views here.

def home(request):
    dados = {}
    funcionario = Funcionario.objects.filter(usuario=request.user)
    dados['contas_caixa'] = ContaCaixa.objects.filter(empresa=funcionario[0].empresa) if funcionario else ""
    return render(request, template_home, dados)

def adicionar(request):
    dados = {}
    dados['form'] = ContaCaixaForm()
    return render(request,template_novo,dados)

def detalhe(request,id,mensagem=''):
    dados = {}
    dados['mensagem'] = mensagem
    conta_caixa = get_object_or_404(ContaCaixa, id=id)
    dados['form'] = ContaCaixaForm(instance=conta_caixa)
    dados['conta_caixa'] = conta_caixa
    return render(request, template_detalhe, dados)

def delete(request,id):
    conta_caixa = ContaCaixa.objects.get(id=id)
    conta_caixa.delete()
    return home(request)

def salvar(request,id):
    dados = {}

    form = ContaCaixaForm(request.POST or None)

    if form.is_valid():
        conta_caixa = form.save(commit=False)

        if id not in (None, '0'):
            conta_caixa.id = id

        conta_caixa.save()
        mensagem = 'Conta-caixa salva com sucesso!'
        return detalhe(request, conta_caixa.id, mensagem)
    else:
        dados['form'] = form
        dados['erros'] = 'Erros nas informações foram encontrados!'
        return render(request, template_novo, dados)

def filtrar(request):
    dados = {}
    contas_caixa = ContaCaixa.objects.filter(descricao__icontains=request.POST['descricao'],
                                             empresa__nome__icontains=request.POST['empresa'],
                                             conta_caixa_superior__descricao__icontains=request.POST['conta_caixa_superior'])
    dados['contas_caixa'] = contas_caixa

    if request.POST.get('relatorio', False):
        dados['data'] = today
        return render(request,template_relatorio,dados)
    else:
        return render(request, template_home,dados)