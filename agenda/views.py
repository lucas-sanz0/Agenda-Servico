import requests

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AgendamentoForm
from .models import Agendamento


@login_required
def lista_agendamentos(request):
    agendamentos = Agendamento.objects.filter(usuario=request.user)
    return render(request, 'agenda/lista_agendamentos.html', {'agendamentos': agendamentos})


@login_required
def detalhe_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
    return render(request, 'agenda/detalhe_agendamento.html', {'agendamento': agendamento})


@login_required
def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.usuario = request.user
            agendamento.save()
            messages.success(request, 'Agendamento criado com sucesso!')
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'agenda/form_agendamento.html', {'form': form, 'titulo': 'Novo agendamento'})


@login_required
def editar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento atualizado com sucesso!')
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'agenda/form_agendamento.html', {'form': form, 'titulo': 'Editar agendamento'})


@login_required
def excluir_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id, usuario=request.user)
    if request.method == 'POST':
        agendamento.delete()
        messages.success(request, 'Agendamento excluído.')
        return redirect('lista_agendamentos')
    return render(request, 'agenda/confirmar_exclusao.html', {'agendamento': agendamento})


def buscar_cep(request, cep):
    try:
        resposta = requests.get('https://viacep.com.br/ws/' + cep + '/json/', timeout=5)
        return JsonResponse(resposta.json())
    except Exception:
        return JsonResponse({'erro': True})
