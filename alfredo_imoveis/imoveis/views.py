# encoding: utf-8
from django.shortcuts import render, get_object_or_404, redirect
from imoveis.models import Imovel, RescisaoContrato
from enderecos.forms import EnderecoForm
from forms import ImovelForm, ContratoLocacaoForm,\
    ContratoAdministrativoForm, LaudoVistoriaForm
from funcionarios.models import Funcionario
from datetime import datetime, date
from imoveis.models import ContratoLocacao,\
    ContratoAdministrativo, LaudoVistoria
from financeiro.models.titulo import Titulo, exclui_parcelas_aberto_contrato_locacao
from parametros.models import ParametrosGerais
from clientes.models import Cliente
from alfredo_imoveis.views import busca_configuracoes
from funcoes import month_between, incrementa_mes
today = date.today()

# Create your views here.
template_home = 'imoveis/home.html'
template_detalhe = 'imoveis/detalhe.html'
template_novo = 'imoveis/novo.html'
template_relatorio = 'imoveis/relatorio.html'

template_contrato_home = 'contrato_locacao/home.html'
template_contrato_detalhe = 'contrato_locacao/detalhe.html'
template_contrato_novo = 'contrato_locacao/novo.html'
template_contrato_imprimir = 'contrato_locacao/imprimir.html'


def dados_base_home(request):
    dados = {}

    funcionario = Funcionario.objects.get(usuario=request.user)
    dados['imoveis'] = Imovel.objects.filter(
        empresa=funcionario.empresa, ativo=True) if funcionario else ""
    return dados


def home(request):
    return render(request, template_home, dados_base_home(request))


def detalhe(request, id, mensagem=''):
    dados = {}
    dados['mensagem'] = mensagem

    imovel = get_object_or_404(Imovel, id=id)

    form_endereco = EnderecoForm(instance=imovel.endereco)
    for field in form_endereco.fields.values():
        field.widget.attrs['disabled'] = True
    dados['formEndereco'] = form_endereco

    form = ImovelForm(instance=imovel)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
    dados['form'] = form

    dados['laudo_vistoria'] = LaudoVistoria.objects.filter(imovel=imovel)
    dados['imovel'] = imovel
    return render(request, template_detalhe, dados)


def editar(request, id, mensagem=''):
    dados = {}
    dados['mensagem'] = mensagem

    dados['modo'] = 'EDICAO'

    imovel = get_object_or_404(Imovel, id=id)

    form_endereco = EnderecoForm(instance=imovel.endereco)
    dados['formEndereco'] = form_endereco

    form = ImovelForm(instance=imovel)
    dados['form'] = form

    dados['laudo_vistoria'] = LaudoVistoria.objects.filter(imovel=imovel)
    dados['imovel'] = imovel
    return render(request, template_detalhe, dados)


def delete(request, id):
    imovel = get_object_or_404(Imovel, id=id)
    imovel.ativo = False
    imovel.save()
    return home(request)


def salvar(request, id):
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
        dados['erros'] = form.errors
        return render(request, template_novo, dados)


def adiciona(request):
    dados = {}
    dados['form'] = ImovelForm()
    dados['formEndereco'] = EnderecoForm()
    return render(request, template_novo, dados)


def filtrar(request):
    dados = {}

    if request.POST.get('data_ini') and request.POST.get('data_fim'):
        dataini = datetime.strptime(request.POST['data_ini'], '%Y-%m-%d')
        datafim = datetime.strptime(request.POST['data_fim'], '%Y-%m-%d')
    else:
        dataini = datetime.strptime('1900-01-01', '%Y-%m-%d')
        datafim = datetime.strptime('2500-12-31', '%Y-%m-%d')

    filtra_inativos = request.POST.get('ativo', False)

    if request.POST.get('codigo'):
        imoveis = Imovel.objects.filter(pk__icontains=request.POST['codigo'])
    else:
        imoveis = Imovel.objects.filter(
            descricao__icontains=request.POST['descricao'],
            data_cadastro__range=[dataini, datafim],
            endereco__rua__icontains=request.POST['rua'],
            endereco__bairro__nome__icontains=request.POST['bairro'],
            endereco__bairro__cidade__nome__icontains=request.POST['cidade'],
            proprietario__nome__icontains=request.POST['proprietario'],
            ativo=not filtra_inativos)

    dados['imoveis'] = imoveis

    if request.POST.get('relatorio', False):
        dados['data'] = today
        return render(request, template_relatorio, dados)
    else:
        return render(request, template_home, dados)


def ficha(request, id):
    dados = {}
    parametros = ParametrosGerais.objects.all()[0]
    dados['imovel'] = Imovel.objects.get(id=id)
    dados['data'] = today
    dados['logo'] = parametros.url_logo
    return render(request, 'imoveis/ficha.html', dados)


def contrato_detalhe(request, id, mensagem=None):
    dados = {}
    dados['mensagem'] = mensagem
    contrato = get_object_or_404(ContratoLocacao, id=id)
    form = ContratoLocacaoForm(instance=contrato)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
    dados['form'] = form
    dados['contrato'] = contrato
    return render(request, template_contrato_detalhe, dados)


def dados_base_contrato_home(request):
    dados = {}
    funcionario = Funcionario.objects.get(usuario=request.user)
    dados['clientes'] = Cliente.objects.filter(
        empresa=funcionario.empresa, ativo=True)
    dados['imoveis'] = Imovel.objects.filter(
        empresa=funcionario.empresa, ativo=True) if funcionario else ""
    dados['contratos'] = ContratoLocacao.objects.filter(
        empresa=funcionario.empresa) if funcionario else ""
    return dados


def contrato_filtrar(request):
    dados = {}

    contratos_locacao = ContratoLocacao.objects.all()

    if request.POST.get('dataini') and request.POST.get('datafim'):
        dataini = datetime.strptime(request.POST['dataini'], '%d/%m/%Y')
        datafim = datetime.strptime(request.POST['datafim'], '%d/%m/%Y')
    else:
        dataini = datetime.strptime('1900-01-01', '%Y-%m-%d')
        datafim = datetime.strptime('2500-12-31', '%Y-%m-%d')

    mes_considerar = request.POST.get('mes', 'nenhum')
    if mes_considerar != 'nenhum':
        if mes_considerar == 'cadastro':
            contratos_locacao = contratos_locacao.filter(
                inicio_contrato__range=[dataini, datafim])
        else:
            contratos_locacao = contratos_locacao.filter(
                termino_contrato__range=[dataini, datafim])

    if request.POST.get('cliente') != '0':
        contratos_locacao = contratos_locacao.filter(
            locatario__id=request.POST.get('cliente'))

    if request.POST.get('imovel') != '0':
        contratos_locacao = contratos_locacao.filter(
            imovel__id=request.POST.get('imovel'))

    dados = dados_base_contrato_home(request)
    dados['contratos'] = contratos_locacao
    return render(request, template_contrato_home, dados)


def contrato_editar(request, id, mensagem=None):
    dados = {}
    dados['mensagem'] = mensagem
    contrato = get_object_or_404(ContratoLocacao, id=id)
    dados['form'] = ContratoLocacaoForm(instance=contrato)
    dados['contrato'] = contrato
    dados['modo'] = 'EDICAO'
    return render(request, template_contrato_detalhe, dados)


def contrato_home(request):
    return render(
        request, template_contrato_home, dados_base_contrato_home(request))


def contrato_salvar(request, id):
    dados = {}

    if id not in (None, '0'):
        contrato = ContratoLocacao.objects.get(id=id)
        form = ContratoLocacaoForm(request.POST or None, instance=contrato)
    else:
        form = ContratoLocacaoForm(request.POST or None)

    if form.is_valid():
        contrato = form.save(commit=False)

        if id not in (None, '0'):
            contrato.id = id
            contrato.data_emissao_contrato =\
                ContratoLocacao.objects.get(id=id).data_emissao_contrato

        contrato.save()
        mensagem = 'Contrato de locação salvo com sucesso!'
        return contrato_detalhe(request, contrato.id, mensagem)
    else:
        dados['form'] = form
        dados['erros'] = 'Erros nas informações foram encontrados!'
        return render(request, template_contrato_novo, dados)


def contrato_imprimir(request, id):
    dados = {}
    dados['data'] = today
    dados['contrato'] = ContratoLocacao.objects.get(id=id)
    return render(request, template_contrato_imprimir, dados)


def contrato_delete(request, id):
    contrato = ContratoLocacao.objects.get(id=id)
    contrato.delete()
    return contrato_home(request)


def contrato_adiciona(request):
    dados = {}
    dados['form'] = ContratoLocacaoForm()
    return render(request, template_contrato_novo, dados)


def contrato_gerar_receber(request, id):
    dados = {}
    contrato = get_object_or_404(ContratoLocacao, id=id)
    parametros = ParametrosGerais.objects.all()

    if contrato.inicio_contrato > contrato.termino_contrato:
        dados['mensagem_erro'] = """
                            As contas a receber deste contrato não
                            foram geradas pois a data inicial de
                            vigência do contrato é maior ou igual a data final,
                            por favor corrija este problema primeiro.
                            """
        return contrato_detalhe(request, id, dados['mensagem_erro'])

    if not parametros[0].conta_caixa:
        dados['mensagem_erro'] = """
                            As contas a receber deste contrato não
                            foram geradas pois não existe uma conta-caixa para
                            contratos informada no cadastro de parâmetros.
                            Por favor resolva este problema antes de continuar
                            """
        return contrato_detalhe(request, id, dados['mensagem_erro'])

    num_parcelas = month_between(
        contrato.inicio_contrato, contrato.termino_contrato) + 1

    funcionario = Funcionario.objects.filter(usuario=request.user)

    if contrato.gerou_receber:
        exclui_parcelas_aberto_contrato_locacao(contrato.id)

    gera_parcelas(
        num_parcelas, contrato.inicio_contrato,
        contrato.imovel.valor_aluguel,
        parametros[0].conta_caixa,
        contrato.locatario, contrato,
        funcionario[0].empresa, request.user)

    dados['mens_parcelas'] =\
        """
        Contas a receber geradas com sucesso:
        Qtd.: {num_parcelas}, Data da primeira parcela:
           {dataini} data da última parcela: {datafim}
        """.format(
        num_parcelas=num_parcelas,
        dataini=contrato.inicio_contrato.strftime("%d/%m/%y"),
        datafim=contrato.termino_contrato.strftime("%d/%m/%y"))

    dados['form'] = ContratoLocacaoForm(instance=contrato)
    contrato.gerou_receber = True
    contrato.save()
    dados['contrato'] = contrato
    return render(request, template_contrato_detalhe, dados)


def gera_parcelas(
    num_parcelas, dataini, valor,
        conta_caixa, cliente, contrato, empresa, usuario):

    msg_confirmacao =\
        'Parcela de locação de imóvel referente ao contrato:{n_cont}'

    for i in range(0, num_parcelas):
        cont_parcelas = str(i + 1) + '-' + str(num_parcelas)
        titulo = Titulo(
            descricao=msg_confirmacao.format(n_cont=contrato.id),
            conta_caixa=conta_caixa, empresa=empresa, tipo='R',
            vencimento=incrementa_mes(dataini, i),
            data_cadastro=today, usuario_cadastrou=usuario, cliente=cliente,
            valor=valor, contrato_locacao=contrato,
            conta_parcelas=cont_parcelas)
        titulo.save()


def adiciona_imovel_para_usuario(request, id_cliente):
    dados = {}
    cliente = Cliente.objects.get(id=id_cliente)
    imovel = Imovel(proprietario=cliente)
    dados['form'] = ImovelForm(instance=imovel)
    dados['formEndereco'] = EnderecoForm()
    return render(request, template_novo, dados)


# Contratos administrativos
def contrato_administrativo_list(
        request,
        template_name=
        'contrato_administrativo/contrato_administrativo_list.html'):
    contratos = ContratoAdministrativo.objects.all()
    data = {}
    data['object_list'] = contratos
    return render(request, template_name, data)


def contrato_administrativo_create(
        request,
        template_name=
        'contrato_administrativo/contrato_administrativo_form.html'):
    form = ContratoAdministrativoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app_imoveis_contrato_administrativo_home')
    return render(request, template_name, {'form': form})


def contrato_administrativo_update(
    request, pk,
    template_name=
        'contrato_administrativo/contrato_administrativo_form_update.html'):
    contrato = get_object_or_404(ContratoAdministrativo, pk=pk)
    form = ContratoAdministrativoForm(request.POST or None, instance=contrato)
    if form.is_valid():
        form.save()
        return redirect('app_imoveis_contrato_administrativo_home')
    return render(
        request,
        template_name, {'form': form, 'object': contrato, 'modo': 'EDICAO'})


def contrato_administrativo_detalhe(
    request, pk,
    template_name=
        'contrato_administrativo/contrato_administrativo_form_update.html'):
    contrato = get_object_or_404(ContratoAdministrativo, pk=pk)
    form = ContratoAdministrativoForm(request.POST or None, instance=contrato)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
    return render(request, template_name, {'form': form, 'object': contrato})


def contrato_administrativo_delete(
    request, pk, template_name=
        'contrato_administrativo/contrato_administrativo_confirm_delete.html'):
    contrato = get_object_or_404(ContratoAdministrativo, pk=pk)
    if request.method == 'POST':
        contrato.delete()
        return redirect('app_imoveis_contrato_administrativo_home')
    return render(request, template_name, {'object': contrato})


def contrato_administrativo_gerar(request, pk):
    dados = {}
    contrato = get_object_or_404(ContratoAdministrativo, pk=pk)
    dados['contrato'] = contrato
    dados['data'] = today
    return render(
        request,
        'contrato_administrativo/imprimir_cintrato.html', dados)


def laudo_vistoria_list(
        request, template_name='laudo_vistoria/laudo_vistoria_list.html'):
    dados = {}

    laudos = LaudoVistoria.objects.all()
    dados['object_list'] = laudos
    return render(request, template_name, dados)


def laudo_vistoria_create(
        request, template_name='laudo_vistoria/laudo_vistoria_form.html',
        pk=None):
    if pk:
        imovel = get_object_or_404(Imovel, pk=pk)
        if imovel:
            laudo = LaudoVistoria(imovel=imovel, data_vistoria=today)
        else:
            laudo = LaudoVistoria()
    else:
            laudo = LaudoVistoria(data_vistoria=today)

    form = LaudoVistoriaForm(request.POST or None, instance=laudo)
    if form.is_valid():
        laudo_vistoria = form.save(commit=False)
        imovel = laudo_vistoria.imovel
        imovel.ultima_vistoria = today
        imovel.save()
        laudo_vistoria.save()
        return redirect('app_imoveis_laudo_vistoria_home')
    return render(request, template_name, {'form': form})


def laudo_vistoria_detalhe(
        request, pk,
        template_name='laudo_vistoria/laudo_vistoria_form_update.html'):
    laudo = get_object_or_404(LaudoVistoria, pk=pk)
    form = LaudoVistoriaForm(request.POST or None, instance=laudo)

    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
    return render(
        request, template_name,
        {'form': form, 'object': laudo})


def laudo_vistoria_update(
        request, pk,
        template_name='laudo_vistoria/laudo_vistoria_form_update.html'):
    laudo = get_object_or_404(LaudoVistoria, pk=pk)
    form = LaudoVistoriaForm(request.POST or None, instance=laudo)
    if form.is_valid():
        form.save()
        return redirect('app_imoveis_laudo_vistoria_home')
    return render(
        request, template_name,
        {'form': form, 'object': laudo, 'modo': 'EDICAO'})


def laudo_vistoria_delete(
        request, pk,
        template_name='laudo_vistoria/laudo_vistoria_confirm_delete.html'):
    laudo = get_object_or_404(LaudoVistoria, pk=pk)
    if request.method == 'POST':
        laudo.delete()
        return redirect('app_imoveis_laudo_vistoria_home')
    return render(request, template_name, {'object': laudo})


def laudo_vistoria_imprimir(
        request, pk,
        template_name='laudo_vistoria/laudo_vistoria_imprimir.html'):
    dados = {}
    busca_configuracoes(request, dados)

    laudo = get_object_or_404(LaudoVistoria, pk=pk)

    dados['laudo'] = laudo
    dados['contrato_locacao'] = ContratoLocacao.objects.filter(
        imovel=laudo.imovel)
    dados['data'] = today
    return render(request, template_name, dados)


def rescindir_contrato(request, id):
    dados = {}
    contrato = get_object_or_404(ContratoLocacao, id=id)
    motivo = request.POST.get('rescisao')
    rescisao = RescisaoContrato(
        contrato=contrato, data=today, usuario=request.user, motivo=motivo)
    rescisao.save()
    exclui_parcelas_aberto_contrato_locacao(contrato.id)
    dados['mensagem'] = 'Contrato rescindido com sucesso!'
    return contrato_detalhe(request, id, dados['mensagem'])
