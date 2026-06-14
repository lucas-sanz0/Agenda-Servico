from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_agendamentos, name='lista_agendamentos'),
    path('novo/', views.criar_agendamento, name='criar_agendamento'),
    path('<int:id>/', views.detalhe_agendamento, name='detalhe_agendamento'),
    path('<int:id>/editar/', views.editar_agendamento, name='editar_agendamento'),
    path('<int:id>/excluir/', views.excluir_agendamento, name='excluir_agendamento'),

    path('api/cep/<str:cep>/', views.buscar_cep, name='buscar_cep'),
]
