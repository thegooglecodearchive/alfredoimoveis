from django.shortcuts import render
from models import Cliente

# Create your views here.
template_home = 'clientes/home.html'

def home(request):
    dados = {}
    dados['clientes'] = Cliente.objects.all()
    return render(request,template_home,dados)