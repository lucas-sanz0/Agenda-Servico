from datetime import date, timedelta

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from agenda.models import Servico


class TestesDeInterface(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opcoes = Options()
        opcoes.add_argument('--headless=new')
        opcoes.add_argument('--window-size=1920,1080')
        cls.navegador = webdriver.Chrome(options=opcoes)
        cls.navegador.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.navegador.quit()
        super().tearDownClass()

    def setUp(self):
        self.usuario = User.objects.create_user(username='joao', password='senhaforte123')
        self.servico = Servico.objects.create(nome='Faxina residencial', preco=150, ativo=True)

    def _clicar(self, elemento):
        self.navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)
        self.navegador.execute_script("arguments[0].click();", elemento)

    def _login(self):
        self.navegador.get(self.live_server_url + '/login/')
        self.navegador.find_element(By.NAME, 'username').send_keys('joao')
        self.navegador.find_element(By.NAME, 'password').send_keys('senhaforte123')
        self.navegador.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        WebDriverWait(self.navegador, 10).until(EC.url_contains('/agendamentos/'))

    def test_home_abre(self):
        self.navegador.get(self.live_server_url + '/')
        self.assertIn('AgendaServiço', self.navegador.title)

    def test_login_com_sucesso(self):
        self._login()
        self.assertIn('/agendamentos/', self.navegador.current_url)

    def test_chatbot_responde(self):
        self.navegador.get(self.live_server_url + '/chatbot/')
        self.navegador.find_element(By.ID, 'campo-mensagem').send_keys('quais serviços vocês oferecem?')
        self._clicar(self.navegador.find_element(By.ID, 'botao-enviar'))
        WebDriverWait(self.navegador, 10).until(
            lambda d: 'faxina' in d.find_element(By.ID, 'conversa').text.lower()
        )
        self.assertIn('faxina', self.navegador.find_element(By.ID, 'conversa').text.lower())

    def test_criar_agendamento(self):
        self._login()
        self.navegador.get(self.live_server_url + '/agendamentos/novo/')
        Select(self.navegador.find_element(By.ID, 'id_servico')).select_by_visible_text('Faxina residencial')
        data_futura = (date.today() + timedelta(days=7)).strftime('%Y-%m-%d')
        self.navegador.execute_script("document.getElementById('id_data').value = arguments[0];", data_futura)
        self.navegador.execute_script("document.getElementById('id_hora').value = '10:00';")
        self.navegador.find_element(By.ID, 'id_cep').send_keys('50030230')
        self.navegador.find_element(By.ID, 'id_numero').send_keys('200')
        self._clicar(self.navegador.find_element(By.CSS_SELECTOR, 'button[type="submit"]'))
        WebDriverWait(self.navegador, 10).until(lambda d: '/novo/' not in d.current_url)
        self.assertIn('Faxina residencial', self.navegador.find_element(By.TAG_NAME, 'body').text)