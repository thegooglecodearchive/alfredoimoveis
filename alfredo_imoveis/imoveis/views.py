# encoding: utf-8
from django.shortcuts import render, get_object_or_404, redirect
from imoveis.models import Imovel
from enderecos.forms import EnderecoForm
from forms import ImovelForm, ContratoLocacaoForm, ContratoAdministrativoForm, LaudoVistoriaForm
from funcionarios.models import Funcionario
from datetime import datetime, date
from imoveis.models import ContratoLocacao, ContratoAdministrativo, LaudoVistoria
from financeiro.models.titulo import Titulo
from parametros.models import ParametrosGerais
from clientes.models import Cliente
from alfredo_imoveis.views import busca_configuracoes
from funcoes import month_between
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

def home(request):
    dados = {}
    #import pdb;pdb.set_trace()
    funcionario = Funcionario.objects.filter(usuario=request.user)
    dados['imoveis'] = Imovel.objects.filter(empresa=funcionario[0].empresa,ativo=True) if funcionario else ""
    return render(request, template_home,dados)

def detalhe(request,id,mensagem=''):
    dados = {}
    dados['mensagem'] = mensagem
    imovel = get_object_or_404(Imovel, id=id)
    dados['formEndereco'] = EnderecoForm(instance=imovel.endereco)
    dados['form'] = ImovelForm(instance=imovel)
    dados['laudo_vistoria'] = LaudoVistoria.objects.filter(imovel=imovel)
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
        dados['erros'] = form.errors
        return render(request, template_novo, dados)


def adiciona(request):
    dados = {}
    dados['form'] = ImovelForm()
    dados['formEndereco'] = EnderecoForm()
    return render(request,template_novo,dados)

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
        imoveis = Imovel.objects.filter(pk__icontains = request.POST['codigo'])
    else:
        imoveis = Imovel.objects.filter(descricao__icontains=request.POST['descricao'],
                                        data_cadastro__range=[dataini,datafim],
                                        endereco__rua__icontains=request.POST['rua'],
                                        endereco__bairro__nome__icontains=request.POST['bairro'],
                                        endereco__bairro__cidade__nome__icontains=request.POST['cidade'],
                                        proprietario__nome__icontains=request.POST['proprietario'],
                                        ativo= not filtra_inativos
                                        )

    dados['imoveis'] = imoveis

    if request.POST.get('relatorio', False):
        dados['data'] = today
        return render(request,template_relatorio,dados)
    else:
        return render(request, template_home,dados)

def ficha(request,id):
    dados = {}
    parametros = get_object_or_404(ParametrosGerais, id=1)
    dados['imovel'] = Imovel.objects.get(id=id)
    dados['data'] = today
    dados['logo'] = parametros.url_logo
    return render(request,'imoveis/ficha.html', dados)

def contrato_detalhe(request,id,mensagem=None):
    dados = {}
    dados['mensagem'] = mensagem
    contrato = get_object_or_404(ContratoLocacao, id=id)
    dados['form'] = ContratoLocacaoForm(instance=contrato)
    dados['contrato'] = contrato
    return render(request, template_contrato_detalhe, dados)

def contrato_home(request):
    dados = {}
    funcionario = Funcionario.objects.filter(usuario=request.user)
    dados['contratos'] = ContratoLocacao.objects.filter(empresa=funcionario[0].empresa) if funcionario else ""
    return render(request,template_contrato_home, dados)

def contrato_salvar(request,id):
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
            contrato.data_emissao_contrato = ContratoLocacao.objects.get(id=id).data_emissao_contrato

        contrato.save()
        mensagem = 'Contrato de locação salvo com sucesso!'
        return contrato_detalhe(request, contrato.id, mensagem)
    else:
        dados['form'] = form
        dados['erros'] = 'Erros nas informações foram encontrados!'
        return render(request, template_contrato_novo, dados)

def contrato_imprimir(request,id):
    dados = {}
    dados['data'] = today
    dados['contrato'] = ContratoLocacao.objects.get(id=id)
    return render(request,template_contrato_imprimir,dados)


def contrato_delete(request,id):
    contrato = ContratoLocacao.objects.get(id=id)
    contrato.delete()
    return contrato_home(request)

def contrato_adiciona(request):
    dados = {}
    dados['form'] = ContratoLocacaoForm()
    return render(request,template_contrato_novo,dados)

def contrato_gerar_receber(request,id):
    dados = {}
    contrato = get_object_or_404(ContratoLocacao,id=id)
    parametros = ParametrosGerais.objects.all()

    if contrato.inicio_contrato > contrato.termino_contrato:
        dados['mensagem_erro'] = """
                            As contas a receber deste contrato não foram geradas pois a data inicial de
                            vigência do contrato é maior ou igual a data final, por favor corrija este problema primeiro.
                            """
        return contrato_detalhe(request,id,dados['mensagem_erro'])

    if not parametros[0].conta_caixa:
        dados['mensagem_erro'] = """
                            As contas a receber deste contrato não foram geradas pois não existe uma conta-caixa para
                            contratos informada no cadastro de parâmetros. Por favor resolva este problema antes de continuar
                            """
        return contrato_detalhe(request,id,dados['mensagem_erro'])

    num_parcelas = month_between(contrato.inicio_contrato, contrato.termino_contrato) + 1

    funcionario = Funcionario.objects.filter(usuario=request.user)

    if contrato.gerou_receber:
        titulos = Titulo.objects.filter(contrato_locacao=contrato)
        titulos.delete()

    gera_parcelas(num_parcelas,contrato.inicio_contrato,contrato.imovel.valor_aluguel,
                  parametros[0].conta_caixa,contrato.locatario,contrato,funcionario[0].empresa,request.user)

    dados['mens_parcelas'] = """Contas a receber geradas com sucesso: Qtd.: {num_parcelas}, Data da primeira parcela:
                           {dataini} data da última parcela: {datafim}
                        """.format(num_parcelas=num_parcelas, dataini=contrato.inicio_contrato.strftime("%d/%m/%y"),
                                                             datafim=contrato.termino_contrato.strftime("%d/%m/%y"))

    dados['form'] = ContratoLocacaoForm(instance=contrato)
    contrato.gerou_receber = True
    contrato.save()
    dados['contrato'] = contrato
    return render(request, template_contrato_detalhe, dados)

def gera_parcelas(num_parcelas,dataini,valor,conta_caixa,cliente,contrato,empresa,usuario):
    venc = dataini

    for i in range(0,num_parcelas):
        titulo = Titulo(descricao='Parcela de locação de imóvel referente ao contrato:{n_cont}'.format(n_cont=contrato.id),
                        conta_caixa=conta_caixa, empresa=empresa,tipo='R',
                        vencimento=date(venc.year, venc.month+i,venc.day),
                        data_cadastro=today, usuario_cadastrou=usuario, cliente=cliente,
                        valor=valor,contrato_locacao=contrato)
        titulo.save()

def adiciona_imovel_para_usuario(request, id_cliente):
    dados = {}
    cliente = Cliente.objects.get(id=id_cliente)
    imovel = Imovel(proprietario=cliente)
    dados['form'] = ImovelForm(instance=imovel)
    dados['formEndereco'] = EnderecoForm()
    return render(request,template_novo,dados)

# Contratos administrativos

def contrato_administrativo_list(request, template_name='contrato_administrativo/contrato_administrativo_list.html'):
    contratos = ContratoAdministrativo.objects.all()
    data = {}
    data['object_list'] = contratos
    return render(request, template_name, data)

def contrato_administrativo_create(request, template_name='contrato_administrativo/contrato_administrativo_form.html'):
    form = ContratoAdministrativoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app_imoveis_contrato_administrativo_home')
    return render(request, template_name, {'form':form})

def contrato_administrativo_update(request, pk, template_name='contrato_administrativo/contrato_administrativo_form_update.html'):
    contrato = get_object_or_404(ContratoAdministrativo, pk=pk)
    form = ContratoAdministrativoForm(request.POST or None, instance=contrato)
    if form.is_valid():
        form.save()
        return redirect('app_imoveis_contrato_administrativo_home')
    return render(request, template_name, {'form':form, 'object':contrato})

def contrato_administrativo_delete(request, pk, template_name='contrato_administrativo/contrato_administrativo_confirm_delete.html'):
    contrato = get_object_or_404(ContratoAdministrativo, pk=pk)    
    if request.method=='POST':
        contrato.delete()
        return redirect('app_imoveis_contrato_administrativo_home')
    return render(request, template_name, {'object':contrato})    

def contrato_administrativo_gerar(request,pk):
    dados = {}
    contrato = get_object_or_404(ContratoAdministrativo, pk=pk)
    dados['contrato'] = contrato
    dados['data'] = today
    return render(request, 'contrato_administrativo/imprimir_cintrato.html', dados)


def laudo_vistoria_list(request, template_name='laudo_vistoria/laudo_vistoria_list.html'):
    dados = {}

    laudos = LaudoVistoria.objects.all()
    dados['object_list'] = laudos
    return render(request, template_name, dados)

def laudo_vistoria_create(request, template_name='laudo_vistoria/laudo_vistoria_form.html', pk=None):
    if pk:
        imovel = get_object_or_404(Imovel,pk=pk)
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
    return render(request, template_name, {'form':form})

def laudo_vistoria_update(request, pk, template_name='laudo_vistoria/laudo_vistoria_form_update.html'):
    laudo = get_object_or_404(LaudoVistoria, pk=pk)
    form = LaudoVistoriaForm(request.POST or None, instance=laudo)
    if form.is_valid():
        form.save()
        return redirect('app_imoveis_laudo_vistoria_home')
    return render(request, template_name, {'form':form, 'object':laudo})    

def laudo_vistoria_delete(request, pk, template_name='laudo_vistoria/laudo_vistoria_confirm_delete.html'):
    laudo = get_object_or_404(LaudoVistoria, pk=pk)    
    if request.method=='POST':
        laudo.delete()
        return redirect('app_imoveis_laudo_vistoria_home')
    return render(request, template_name, {'object':laudo})    

def laudo_vistoria_delete(request,pk,template_name='laudo_vistoria/laudo_vistoria_imprimir.html'):    
    dados = {}
    busca_configuracoes(request,dados)
    
    laudo = get_object_or_404(LaudoVistoria,pk=pk)
    
    dados['laudo'] = laudo
    dados['contrato_locacao'] = ContratoLocacao.objects.filter(imovel = laudo.imovel)
    dados['data'] = today
    return render(request,template_name,dados)