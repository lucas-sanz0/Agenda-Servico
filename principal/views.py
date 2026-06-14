from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from agenda.models import Servico
from .forms import CadastroUsuarioForm


def home(request):
    servicos = Servico.objects.filter(ativo=True)
    return render(request, 'home.html', {'servicos': servicos})


def cadastro(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Cadastro realizado com sucesso! Bem-vindo(a).')
            return redirect('lista_agendamentos')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'principal/cadastro.html', {'form': form})
