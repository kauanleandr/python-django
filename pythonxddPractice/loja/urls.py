# loja/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('chat/', views.chatbot_view, name='chatbot'),  # Página do chatbot com interface
    path('api/chatbot/', views.chatbot_api, name='chatbot_api'),  # API de respostas
]
