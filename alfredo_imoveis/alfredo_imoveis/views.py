__author__ = 'gpzim98'
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

template_home = 'index.html'
template_dashboard = 'dashboard.html'


def home(request):
    if request.user.is_authenticated():
        return dashboard(request)
    else:
        return redirect('url_login')

@login_required
def dashboard(request):
    dados = {}
    return render(request, template_dashboard, dados)