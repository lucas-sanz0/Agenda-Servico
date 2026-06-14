from django.contrib.auth.models import User
from django.db import models


class Servico(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', blank=True)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    STATUS_ESCOLHAS = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agendamentos')
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    data = models.DateField('Data')
    hora = models.TimeField('Hora')
    # endereço preenchido pela ViaCEP
    cep = models.CharField('CEP', max_length=9)
    logradouro = models.CharField('Logradouro', max_length=150, blank=True)
    numero = models.CharField('Número', max_length=10)
    complemento = models.CharField('Complemento', max_length=100, blank=True)
    bairro = models.CharField('Bairro', max_length=100, blank=True)
    cidade = models.CharField('Cidade', max_length=100, blank=True)
    uf = models.CharField('UF', max_length=2, blank=True)
    observacoes = models.TextField('Observações', blank=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_ESCOLHAS, default='pendente')
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        ordering = ['-data', 'hora']

    def __str__(self):
        return f'{self.servico} - {self.data} {self.hora}'
