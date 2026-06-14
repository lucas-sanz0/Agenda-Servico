from datetime import date, timedelta

from django.test import TestCase

from .forms import AgendamentoForm
from .models import Servico


class AgendamentoFormTests(TestCase):
    def setUp(self):
        self.servico = Servico.objects.create(nome='Faxina residencial', preco=150, ativo=True)

    def _dados(self, data_str):
        return {
            'servico': self.servico.id, 'data': data_str, 'hora': '10:00',
            'cep': '50000000', 'numero': '100', 'logradouro': 'Rua Teste',
            'bairro': 'Centro', 'cidade': 'Recife', 'uf': 'PE',
            'observacoes': '', 'complemento': '',
        }

    def test_data_passada_eh_invalida(self):
        ontem = date.today() - timedelta(days=1)
        form = AgendamentoForm(data=self._dados(ontem.strftime('%Y-%m-%d')))
        self.assertFalse(form.is_valid())

    def test_data_futura_eh_valida(self):
        futuro = date.today() + timedelta(days=3)
        form = AgendamentoForm(data=self._dados(futuro.strftime('%Y-%m-%d')))
        self.assertTrue(form.is_valid())
