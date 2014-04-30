from django.shortcuts import render, get_object_or_404
from models import Funcionario
from forms import FuncionarioForm
# Create your views here.

template_home = 'funcionarios/home.html'
template_add = 'funcionarios/funcionario_add.html'

def home(request):
    dados = {}
    funcionarios = Funcionario.objects.all().order_by('id')
    dados['funcionarios'] = funcionarios
    return render(request,template_home,dados)

def adiciona(request):
    dados = {}
    form = FuncionarioForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return home(request)
        else:
            dados['form'] = form
    else:
        dados['form'] = form
        return render(request, template_add, dados)

def delete(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()
    return home(request)

def detalhe(request, id):
    dados = {}
    funcionario = get_object_or_404(Funcionario, id=id)
    form = FuncionarioForm(instance=funcionario)
    dados['form'] = form
    dados['funcionario'] = funcionario
    dados['detalhe'] = 'detalhe'
    return render(request,template_add,dados)

def update(request, id):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        funcionario = form.save(commit=False)
        funcionario.id = id
        funcionario .save()
        return home(request)
    else:
        dados = {}
        dados['form'] = form