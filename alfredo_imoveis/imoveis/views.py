# encoding: utf-8
from django.shortcuts import render, get_object_or_404
from imoveis.models import Imovel
from enderecos.forms import EnderecoForm
from forms import ImovelForm
from funcionarios.models import Funcionario
from datetime import datetime, date

today = date.today()

# Create your views here.
template_home = 'imoveis/home.html'
template_detalhe = 'imoveis/detalhe.html'
template_novo = 'imoveis/novo.html'
template_relatorio = 'imoveis/relatorio.html'

def home(request):
    dados = {}
    #import pdb;pdb.set_trace()
    funcionario = Funcionario.objects.filter(usuario=request.user)
    dados['imoveis'] = Imovel.objects.filter(empresa=funcionario[0].empresa)
    return render(request, template_home,dados)

def detalhe(request,id,mensagem=''):
    dados = {}
    dados['mensagem'] = mensagem
    imovel = get_object_or_404(Imovel, id=id)
    dados['formEndereco'] = EnderecoForm(instance=imovel.endereco)
    dados['form'] = ImovelForm(instance=imovel)
    dados['imovel'] = imovel
    return render(request, template_detalhe, dados)

def delete(request,id):
    imovel = get_object_or_404(Imovel, id=id)
    imovel.ativo = False
    imovel.save()
    return home(request)

def salvar(request,id):
    dados = {}

    form = ImovelForm(request.POST or None)
    formEndereco = EnderecoForm(request.POST or None)

    if form.is_valid() and formEndereco.is_valid():
        imovel = form.save(commit=False)

        if id not in (None, '0'):
            imovel.id = id
            imovel.data_cadastro = Imovel.objects.get(id=id).data_cadastro

        imovel.endereco = formEndereco.save()

        imovel.save()
        mensagem = 'Imóvel salvo com sucesso!'
        return detalhe(request, imovel.id, mensagem)
    else:
        dados['form'] = form
        dados['formEndereco'] = formEndereco
        dados['erros'] = 'Erros nas informações foram encontrados!'
        return render(request, template_novo, dados)


def adiciona(request):
    dados = {}
    dados['form'] = ImovelForm()
    dados['formEndereco'] = EnderecoForm()
    return render(request,template_novo,dados)

def filtrar(request):
    dados = {}
    #imoveis = Imovel.objects.all()

    if request.POST['dataini'] and request.POST['datafim']:
        dataini = datetime.strptime(request.POST['dataini'], '%Y-%m-%d')
        datafim = datetime.strptime(request.POST['datafim'], '%Y-%m-%d')
    else:
        dataini = datetime.strptime('1900-01-01', '%Y-%m-%d')
        datafim = datetime.strptime('2500-12-31', '%Y-%m-%d')

    filtra_inativos = request.POST.get('ativo', False)

    imoveis = Imovel.objects.filter(descricao__contains=request.POST['descricao'],
                                    data_cadastro__range=[dataini,datafim],
                                    endereco__rua__contains=request.POST['rua'],
                                    endereco__bairro__nome__contains=request.POST['bairro'],
                                    endereco__bairro__cidade__nome__contains=request.POST['cidade'],
                                    proprietario__nome__contains=request.POST['proprietario'],
                                    ativo=not filtra_inativos)

    dados['imoveis'] = imoveis

    if request.POST.get('relatorio', False):
        dados['data'] = today
        return render(request,template_relatorio,dados)
    else:
        return render(request, template_home,dados)

def ficha(request,id):
    dados = {}
    dados['imovel'] = Imovel.objects.get(id=id)
    dados['data'] = today
    return render(request,'imoveis/ficha.html', dados)