from django.contrib import admin

from .models import Agendamento, Servico


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'ativo']
    list_filter = ['ativo']
    search_fields = ['nome']


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ['servico', 'usuario', 'data', 'hora', 'status']
    list_filter = ['status', 'data']
    search_fields = ['usuario__username', 'cidade']
