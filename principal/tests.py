from django.test import TestCase
from django.urls import reverse


class HomeTests(TestCase):

    def test_home_responde_200(self):
        resposta = self.client.get(reverse('home'))
        self.assertEqual(resposta.status_code, 200)
