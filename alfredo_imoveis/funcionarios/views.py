# encoding:utf8
from django.shortcuts import render, get_object_or_404
from models import Funcionario
from forms import FuncionarioForm
from enderecos.forms import EnderecoForm

template_home = 'funcionarios/home.html'
template_add = 'funcionarios/funcionario_add.html'
template_detalhe = 'funcionarios/funcionario_detalhe.html'

def home(request,dados={}):
    funcionarios = Funcionario.objects.all().order_by('id')
    dados['funcionarios'] = funcionarios
    return render(request,template_home,dados)

def adiciona(request):
    dados = {}
    form = FuncionarioForm(request.POST or None)
    formEndereco = EnderecoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid() and formEndereco.is_valid():
            funcionario = form.save(commit=False)
            funcionario.endereco = formEndereco.save()
            funcionario.save()
            dados['mensagem'] = 'Funcionário {nome} cadastrado com sucesso'.format(nome=funcionario.nome)
            return home(request,dados)
        else:
            dados['form'] = form
            dados['formEndereco'] = formEndereco
            dados['erros'] = form.errors
            return render(request, template_add, dados)
    else:
        dados['form'] = form
        dados['formEndereco'] = formEndereco
        return render(request, template_add, dados)

def delete(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()
    return home(request)

def detalhe(request, id):
    dados = {}
    funcionario = get_object_or_404(Funcionario, id=id)
    dados['form'] = FuncionarioForm(instance=funcionario)
    dados['formEndereco'] = EnderecoForm(instance=funcionario.endereco)
    dados['funcionario'] = funcionario
    dados['detalhe'] = 'detalhe'
    return render(request,template_add,dados)

def update(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    form = FuncionarioForm(request.POST or None, instance=funcionario)
    formEndereco = EnderecoForm(request.POST or None, instance=funcionario.endereco)
    if form.is_valid() and formEndereco.is_valid():
        funcionario = form.save(commit=False)
        funcionario.enderecos = formEndereco.save()
        funcionario.id = id
        funcionario .save()
        return home(request)
    else:
        dados = {}
        dados['form'] = form
        dados['detalhe'] = 'detalhe'
        dados['funcionario'] = funcionario
        return render(request,template_add,dados)