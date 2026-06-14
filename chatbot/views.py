import unicodedata

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .base_conhecimento import INTENCOES, RESPOSTA_PADRAO


def normalizar(texto):
    # minúsculo e sem acento, pra comparar ("Serviço"  "servico")
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    return ''.join(c for c in texto if not unicodedata.combining(c))


def descobrir_resposta(mensagem):
    # conta quantas palavras-chave batem;
    texto = normalizar(mensagem)
    melhor_intencao = None
    melhor_pontuacao = 0
    for intencao in INTENCOES:
        pontuacao = 0
        for palavra in intencao['palavras_chave']:
            if normalizar(palavra) in texto:
                pontuacao = pontuacao + 1
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_intencao = intencao
    if melhor_intencao is None:
        return RESPOSTA_PADRAO
    return melhor_intencao['resposta']


def pagina_chat(request):
    return render(request, 'chatbot/chat.html')


@require_POST
def responder(request):
    resposta = descobrir_resposta(request.POST.get('mensagem', ''))
    return JsonResponse({'resposta': resposta})
