from django.test import TestCase

from .views import normalizar, descobrir_resposta


class ChatbotTests(TestCase):

    def test_normalizar_remove_acento(self):
        self.assertEqual(normalizar('Serviço'), 'servico')

    def test_reconhece_pergunta_de_preco(self):
        resposta = descobrir_resposta('quanto custa a faxina?')
        self.assertIn('R$', resposta)

    def test_pergunta_desconhecida_usa_resposta_padrao(self):
        resposta = descobrir_resposta('qual a capital da mongolia')
        self.assertIn('não entendi', resposta)
