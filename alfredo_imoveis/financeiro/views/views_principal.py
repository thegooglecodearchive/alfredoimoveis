from django.shortcuts import render

template_home = 'financeiro/home.html'
# Create your views here.

def home(request):
    dados = {}
    return render(request, template_home, dados)
