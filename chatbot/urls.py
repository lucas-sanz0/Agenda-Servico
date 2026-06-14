from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_chat, name='pagina_chat'),
    path('responder/', views.responder, name='responder'),
]
