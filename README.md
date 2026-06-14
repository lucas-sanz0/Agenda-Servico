# AgendaServiço

Site de agendamento de serviços a domicílio (faxina, jardinagem e pequenos reparos). É o nosso Projeto Integrador, juntando a parte de desenvolvimento web (Django), os testes (Selenium) e a inteligência artificial (um chatbot). Também usa a API ViaCEP pra preencher o endereço pelo CEP.

## Integrantes

- João Lucas Barbosa dos Santos
- Keveley Roberta Elias da Silva
- Juliane Andrade da Silva

## Tecnologias usadas

- Python
- Django 5.2
- SQLite
- Bootstrap 5
- requests (pra consumir a ViaCEP)
- Selenium (pros testes)

## Como rodar

Cria e ativa o ambiente virtual.

No Windows:
```
python -m venv venv
venv\Scripts\activate
```

Instala as dependências:
```
pip install -r requirements.txt
```

Cria o banco e carrega os serviços:
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata servicos_iniciais
```

Cria um usuário admin:
```
python manage.py createsuperuser
```

Roda o servidor:
```
python manage.py runserver
```

Aí é só abrir http://127.0.0.1:8000/ no navegador. O admin fica em http://127.0.0.1:8000/admin/.

obs: usa o Python 3.12 ou 3.13. no 3.14 dá um erro de incompatibilidade com versões mais antigas do Django.

## Usuários de teste

- usuário comum: dá pra criar um na própria tela de cadastro do site
- admin: é o superuser que você cria no createsuperuser

## Testes

Pra rodar:
```
python manage.py test
```

Os testes do Selenium abrem o Chrome sozinho, então precisa ter o Google Chrome instalado.
