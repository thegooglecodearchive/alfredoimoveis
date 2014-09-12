# encoding: utf8
from django.shortcuts import render
from financeiro.models.titulo import Titulo, ContaCaixa
from datetime import datetime, date
from django.db.models import Sum

today = date.today()

template_home = 'financeiro/caixa/home.html'
template_relatorio = 'financeiro/caixa/relatorio.html'


def contabiliza_totais_dia():
    dados = {}
    entradas = Titulo.objects.filter(
        data_quitacao=today, tipo='R').aggregate(Sum('pagamento_parcial'))
    saidas = Titulo.objects.filter(
        data_quitacao=today, tipo='D').aggregate(Sum('pagamento_parcial'))

    entradas = entradas['pagamento_parcial__sum']\
        if entradas['pagamento_parcial__sum'] else 0
    saidas = saidas['pagamento_parcial__sum']\
        if saidas['pagamento_parcial__sum'] else 0

    dados['entradas'] = entradas
    dados['saidas'] = saidas
    dados['saldo'] = entradas - saidas
    return dados


def home(request):
    dados = {}
    titulos = Titulo.objects.filter(data_quitacao=today)
    dados = contabiliza_totais_dia()
    dados['titulos'] = titulos
    dados['contas_caixa'] = ContaCaixa.objects.all()
    return render(request, template_home, dados)


def filtra_titulos(request):
    dados = {}

    dados = contabiliza_totais_dia()

    titulos = Titulo.objects.all()

    if request.POST['contas_cx'] != '0':
        titulos = titulos.filter(conta_caixa=request.POST['contas_cx'])

    if request.POST['tipo'] in ('R', 'D'):
        titulos = titulos.filter(tipo=request.POST['tipo'])

    if request.POST['dataini'] and request.POST['datafim']:
        dataini = datetime.strptime(request.POST['dataini'], '%d/%m/%Y')
        datafim = datetime.strptime(request.POST['datafim'], '%d/%m/%Y')
    else:
        dataini = today
        datafim = today

    titulos = titulos.filter(data_quitacao__range=[dataini, datafim])

    dados['contas_caixa'] = ContaCaixa.objects.all()
    dados['titulos'] = titulos

    if request.POST.get('relatorio', False):
        dados['data'] = today
        return render(request, template_relatorio, dados)
    else:
        return render(request, template_home, dados)
