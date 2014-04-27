# encoding: utf8
from django.shortcuts import render, get_object_or_404
from models import Cliente
from forms import ClienteForm
from enderecos.models import Endereco
from enderecos.forms import EnderecoForm
import datetime

today = datetime.date.today()


# Create your views here.
template_home = 'clientes/home.html'
template_novo = 'clientes/novo.html'
template_detalhe = 'clientes/detalhe.html'

def home(request):
    dados = {}
    dados['clientes'] = Cliente.objects.all()
    return render(request,template_home,dados)

def novo(request):
    dados = {}
    dados['form'] = ClienteForm()
    dados['formEndereco'] = EnderecoForm()
    return render(request,template_novo,dados)

def salvar(request, id=None):
    dados = {}

    form = ClienteForm(request.POST or None)
    formEndereco = EnderecoForm(request.POST or None)

    if form.is_valid() and formEndereco.is_valid():
        cliente = form.save(commit=False)

        if id not in (None, '0'):
            cliente.id = id

        cliente.endereco = formEndereco.save()
        cliente.save()
        mensagem = 'Cliente salvo com sucesso!'
        return detalhe(request, cliente.id, mensagem)
    else:
        dados['form'] = form
        dados['formEndereco'] = formEndereco
        dados['erros'] = 'Erros nas informações foram encontrados!'
        return render(request, template_novo, dados)

def detalhe(request,id,mensagem=None):
    dados = {}
    dados['mensagem'] = mensagem
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(instance=cliente)
    dados['formEndereco'] = EnderecoForm(instance=cliente.endereco)
    dados['form'] = form
    dados['cliente'] = cliente
    return render(request, template_detalhe, dados)

def relatorios(request):
    pass

def delete(request,id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return home(request)
