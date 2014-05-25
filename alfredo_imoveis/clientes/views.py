# encoding: utf8
from django.shortcuts import render, get_object_or_404
from models import Cliente
from forms import ClienteForm
from enderecos.models import Endereco
from enderecos.forms import EnderecoForm
from datetime import datetime, date
from imoveis.models import Imovel
from funcionarios.models import Funcionario

today = date.today()

# Create your views here.
template_home = 'clientes/home.html'
template_novo = 'clientes/novo.html'
template_detalhe = 'clientes/detalhe.html'
template_relatorio = 'clientes/relatorio.html'

def home(request):
    dados = {}
    dados['clientes'] = Cliente.objects.filter(ativo=True).order_by('nome')
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
            cliente.data_cadastro = Cliente.objects.get(id=id).data_cadastro

        cliente.endereco = formEndereco.save()
        
        empresa = Funcionario.objects.get(usuario=request.user).empresa
        cliente.empresa = empresa
        cliente.ativo = True
        cliente.save()
        mensagem = 'Cliente salvo com sucesso!'
        return detalhe(request, cliente.id, mensagem)
    else:
        dados['form'] = form
        dados['formEndereco'] = formEndereco
        dados['erros'] = form.errors 
        return render(request, template_novo, dados)

def detalhe(request,id,mensagem=None):
    dados = {}
    dados['mensagem'] = mensagem
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(instance=cliente)
    dados['form'] = form
    dados['formEndereco'] = EnderecoForm(instance=cliente.endereco)
    dados['cliente'] = cliente
    dados['imoveis'] = Imovel.objects.filter(proprietario=cliente)
    return render(request, template_detalhe, dados)

def delete(request,id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.ativo = False
    cliente.save()
    return home(request)

def filtrar(request):
    dados = {}

    clientes = Cliente.objects.all()

    if request.POST['nome']:
        clientes = clientes.filter(nome__contains = request.POST['nome'])
    if request.POST['codigo']:
        clientes = clientes.filter(id = request.POST['codigo'])

    if request.POST['endereco']:
        if clientes.filter(endereco__rua__contains = request.POST['endereco']):
            clientes = clientes.filter(endereco__rua__contains = request.POST['endereco'])

        if clientes.filter(endereco__bairro__nome__contains = request.POST['endereco']):
            clientes = clientes.filter(endereco__bairro__nome__contains = request.POST['endereco'])

        if clientes.filter(endereco__bairro__cidade__nome__contains = request.POST['endereco']):
            clientes = clientes.filter(endereco__bairro__cidade__nome__contains = request.POST['endereco'])

        if clientes.filter(endereco__bairro__cidade__uf__contains = request.POST['endereco']):
            clientes = clientes.filter(endereco__bairro__cidade__uf__contains = request.POST['endereco'])

    if request.POST.get('ativo', False):
        clientes = clientes.filter(ativo=False)
    else:
        clientes = clientes.filter(ativo=True)

    if request.POST['dataini'] and request.POST['datafim']:
        dataini = datetime.strptime(request.POST['dataini'], '%Y-%m-%d')
        datafim = datetime.strptime(request.POST['datafim'], '%Y-%m-%d')
        clientes = clientes.filter(data_cadastro__range=[dataini,datafim])

    if not clientes:
        dados['clientes'] = Cliente.objects.all()
        dados['mensagem'] = 'Nenhum cliente encontrado para esta pesquisa'
    dados['clientes'] = clientes

    if request.POST.get('relatorio', False):
        dados['data'] = today
        return render(request,template_relatorio,dados)
    else:
        return render(request,template_home,dados)

def tabela(request):
    return render(request,'tabela2.html')    

def relatorio(request):
    pass    

def relatorios(request):
    pass
