# encoding: utf8
__author__ = 'gpzim98'
from django.shortcuts import render, get_object_or_404
from financeiro.models.titulo import Titulo, Recibo
from financeiro.models.conta_caixa import ContaCaixa
from funcionarios.models import Funcionario
from financeiro.forms.titulo import TituloForm
from parametros.models import ParametrosGerais
from clientes.models import Cliente
from datetime import datetime, date
from decimal import *
from funcoes import month_between, days_between, calcula_meses_atraso, today
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

template_home = 'financeiro/titulo/home.html'
template_novo = 'financeiro/titulo/novo.html'
template_detalhe = 'financeiro/titulo/detalhe.html'
template_relatorio = 'financeiro/titulo/relatorio.html'
template_recibo = 'financeiro/titulo/recibo.html'
template_carta_cobranca_modelo_1 = 'financeiro/titulo/carta_cobranca_modelo_1.html'
template_carta_cobranca_modelo_2 = 'financeiro/titulo/carta_cobranca_modelo_2.html'
template_carta_cobranca_modelo_3 = 'financeiro/titulo/carta_cobranca_modelo_3.html'

def home(request):
    dados = {}
    funcionario = Funcionario.objects.filter(usuario=request.user)
    dados['titulos'] = Titulo.objects.filter(empresa=funcionario[0].empresa, deletado=False) if funcionario else ""
    dados['mensagem_erro'] = verifica_existencia_parametros()
    dados['clientes'] = Cliente.objects.all()
    dados['contas_caixa'] = ContaCaixa.objects.all()
    return render(request, template_home, dados)

def detalhe(request,id,mensagem=''):
    dados = {}
    dados['mensagem'] = mensagem
    titulo = get_object_or_404(Titulo, id=id)
    dados['form'] = TituloForm(instance=titulo)
    dados['titulo'] = titulo
    recibos = Recibo.objects.filter(titulo=titulo)
    dados['recibos'] = recibos
    return render(request, template_detalhe, dados)

def delete(request, id):
    titulo = Titulo.objects.get(id=id)
    titulo.deletado = True
    titulo.save()
    return home(request)

def filtrar(request):
    dados = {}

    dados['titulos'] = filtra_titulos(request)

    if request.POST.get('relatorio', False):
        dados['data'] = today
        return render(request,template_relatorio,dados)
    else:
        dados['clientes'] = Cliente.objects.all()
        dados['contas_caixa'] = ContaCaixa.objects.all()
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
        dados['erros'] = form.errors
        return render(request, template_novo, dados)

def adicionar(request):
    dados = {}
    dados['mensagem_erro'] = verifica_existencia_parametros()
    dados['form'] = TituloForm()
    return render(request, template_novo, dados)

def recibo(request,id):
    dados = {}
    titulo = get_object_or_404(Titulo,pk=id)
    recibo = Recibo(titulo=titulo, data_cadastro=today,usuario=request.user,descricao='...')
    recibo.save()
    dados['recibo'] = recibo
    return render(request, template_recibo, dados)

def carta_cobranca_modelo_1(request,id):
    dados = {}
    dados['data'] = today
    dados['titulos'] = Titulo.objects.filter(id=id)
    return render(request, template_carta_cobranca_modelo_1,dados)

def carta_cobranca_modelo_2(request,id):
    dados = {}
    dados['data'] = today
    dados['titulos'] = Titulo.objects.filter(id=id)
    data_de = date(Titulo.objects.filter(id=id)[0].vencimento.year, Titulo.objects.filter(id=id)[0].vencimento.month+1,Titulo.objects.filter(id=id)[0].vencimento.day)
    dados['periodo_de'] = Titulo.objects.filter(id=id)[0].vencimento
    dados['periodo_ate'] = data_de
    return render(request, template_carta_cobranca_modelo_2,dados)

def carta_cobranca_modelo_3(request,id):
    dados = {}
    dados['data'] = today
    dados['titulos'] = Titulo.objects.filter(id=id)
    return render(request, template_carta_cobranca_modelo_3,dados)    

def abater_titulo(request,id):
    dados = {}
    titulo = get_object_or_404(Titulo, pk=id)
    titulo.abater_valor(request.POST.get('valor',0))
    url = reverse('app_financeiro_titulo_detalhe', kwargs={'id':id})
    return redirect(url)

def verifica_existencia_parametros():
    return U"""ATENÇÃO, configure os parâmetros antes de prosseguir com a operação,  
        a falta destes pode causar problemas na gravação do registro"""  if ParametrosGerais.objects.all().count() == 0 else ""

def filtra_titulos(request):
    titulos = Titulo.objects.all()
    
    if request.POST['cliente'] != '0':
        titulos = Titulo.objects.filter(cliente__id=request.POST['cliente'])

    if request.POST['contas_cx'] != '0':
        titulos = titulos.filter(conta_caixa=request.POST['contas_cx'])

    if request.POST['tipo'] in ('R', 'D'):
        titulos = titulos.filter(tipo=request.POST['tipo']) 
    
    if request.POST.get('valor_titulo', False):
        valorini=float(request.POST.get('valor_titulo', False))
        valorfim=float(request.POST.get('valor_titulo', False))
    else:
        valorini=0
        valorfim=999999
    titulos = titulos.filter(valor__range=[valorini,valorfim]) 

    if request.POST['dataini'] and request.POST['datafim']:
        dataini = datetime.strptime(request.POST['dataini'], '%d/%m/%Y')
        datafim = datetime.strptime(request.POST['datafim'], '%d/%m/%Y')
    else:
        dataini = datetime.strptime('1900-01-01', '%Y-%m-%d')
        datafim = datetime.strptime('2500-01-01', '%Y-%m-%d')
    titulos = titulos.filter(vencimento__range=[dataini, datafim]) 

    titulos = titulos.filter(descricao__icontains=request.POST['descricao'])
    titulos = titulos.filter(deletado=request.POST.get('deletados', False))
    titulos = titulos.filter(empresa__nome__icontains=request.POST['empresa'])

    return titulos        

def cartas_cobranca_automatizada(request):
    dados = {}

    dados['clientes'] = Cliente.objects.filter(ativo=True)
    dados['contas_caixa'] = ContaCaixa.objects.all()
    return render(request,'financeiro/titulo/cartas_cobranca_automatizada.html', dados)  

def cartas_cobranca_automatizada_filtrar(request):
    dados = {}

    dados['titulos'] = filtra_titulos(request)

    if request.POST.get('imprimir', False):
        dados['data'] = today
        return render(request,get_modelo_carta(request),dados)
    else:
        dados['contas_caixa'] = ContaCaixa.objects.all()
        dados['clientes'] = Cliente.objects.filter(ativo=True)
        return render(request,'financeiro/titulo/cartas_cobranca_automatizada.html', dados)        

def get_modelo_carta(request):
    if request.POST['modelo_carta'] == 'M1':
        return template_carta_cobranca_modelo_1
    elif request.POST['modelo_carta'] == 'M2':
        return template_carta_cobranca_modelo_2
    else:
        return template_carta_cobranca_modelo_3
