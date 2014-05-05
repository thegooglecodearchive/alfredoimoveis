# encoding: utf8
__author__ = 'gpzim98'
from django.shortcuts import render, get_object_or_404
from financeiro.models.titulo import Titulo
from funcionarios.models import Funcionario
from financeiro.forms.titulo import TituloForm
from datetime import datetime, date

today = date.today()

template_home = 'financeiro/titulo/home.html'
template_novo = 'financeiro/titulo/novo.html'
template_detalhe = 'financeiro/titulo/detalhe.html'
template_relatorio = 'financeiro/titulo/relatorio.html'

def home(request):
    dados = {}
    funcionario = Funcionario.objects.filter(usuario=request.user)
    dados['titulos'] = Titulo.objects.filter(empresa=funcionario[0].empresa, deletado=False)
    return render(request, template_home, dados)

def detalhe(request,id,mensagem=''):
    dados = {}
    dados['mensagem'] = mensagem
    titulo = get_object_or_404(Titulo, id=id)
    dados['form'] = TituloForm(instance=titulo)
    dados['titulo'] = titulo
    return render(request, template_detalhe, dados)

def delete(request, id):
    titulo = Titulo.objects.get(id=id)
    titulo.deletado = True
    titulo.save()
    return home(request)

def filtrar(request):
    dados = {}

    if request.POST['dataini'] and request.POST['datafim']:
        dataini = datetime.strptime(request.POST['dataini'], '%Y-%m-%d')
        datafim = datetime.strptime(request.POST['datafim'], '%Y-%m-%d')
    else:
        dataini = datetime.strptime('1900-01-01', '%Y-%m-%d')
        datafim = datetime.strptime('2500-12-31', '%Y-%m-%d')

    if request.POST.get('valor_titulo', False):
        valorini=float(request.POST.get('valor_titulo', False))
        valorfim=float(request.POST.get('valor_titulo', False))
    else:
        valorini=0
        valorfim=999999

    if request.POST['tipo'] in ('R', 'D'):
        tipo = request.POST['tipo']
    else:
        tipo = ''

    dados['titulos'] = Titulo.objects.filter(empresa__nome__contains=request.POST['empresa'],
                                             deletado=request.POST.get('deletados', False),
                                             descricao__contains=request.POST['descricao'],
                                             conta_caixa__descricao__contains=request.POST['conta_caixa'],
                                             vencimento__range=[dataini, datafim],
                                             valor__range=[valorini, valorfim],
                                             tipo__contains=tipo)

    if request.POST.get('relatorio', False):
        dados['data'] = today
        return render(request,template_relatorio,dados)
    else:
        return render(request, template_home,dados)

def salvar(request,id):
    dados = {}

    form = TituloForm(request.POST or None)

    if form.is_valid():
        titulo = form.save(commit=False)

        if id not in (None, '0'):
            titulo.id = id

        titulo.usuario_cadastrou = request.user
        titulo.data_cadastro = today
        titulo.save()
        mensagem = 'Título salvo com sucesso!'
        return detalhe(request, titulo.id, mensagem)
    else:
        dados['form'] = form
        dados['erros'] = 'Erros nas informações foram encontrados!'
        return render(request, template_novo, dados)

def adicionar(request):
    dados = {}
    dados['form'] = TituloForm()
    return render(request, template_novo, dados)

#def gera_conta()