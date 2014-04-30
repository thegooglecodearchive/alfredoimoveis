from django.shortcuts import render, get_object_or_404
from forms import BairroForm
from models import Bairro

# Create your views here.
template_bairro_novo = 'enderecos/bairro/bairro.html'
template_bairro_add = 'enderecos/bairro/bairro_add.html'

def bairro_home(request):
    dados = {}
    dados['lista_bairros'] = Bairro.objects.all().order_by('id')
    form = BairroForm()
    dados['form'] = form
    return render(request,template_bairro_novo,dados)

def bairro_detalhe(request, id):
    dados = {}
    bairro = get_object_or_404(Bairro, id=id)
    form = BairroForm(instance=bairro)
    dados['lista_bairros'] = Bairro.objects.all()
    dados['form'] = form
    return render(request,template_bairro_add,dados)

def bairro_adiciona(request):
    dados = {}
    form = BairroForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return bairro_home(request)
        else:
            dados['form'] = form
    else:
        dados['form'] = form
        return render(request, template_bairro_add, dados)

def bairro_update(request, id):
    form = BairroForm(request.POST or None)
    if form.is_valid():
        bairro = form.save(commit=False)
        bairro.id = id
        bairro.save()
        return bairro_home(request)
    else:
        dados = {}
        dados['form'] = form

def bairro_delete(request, id):
    bairro = Bairro.objects.get(id=id)
    bairro.delete()
    return bairro_home(request)