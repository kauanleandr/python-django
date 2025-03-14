# loja/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json

def home(request):
    return HttpResponse("<h1>Bem-vindo ao Chatbot com Django!</h1>")

# Função para gerar resposta simples (simulada)
def chatbot_response(user_message):
    responses = {
        "oi": "oi como posso ajudar?",
        "como ta essa força?": "forca? so se for cerebrau ne? kkkkk",
    }
    if user_message is None:
        return "Por favor, envie uma mensagem para que eu possa responder."
    return responses.get(user_message.lower(), "Desculpe, nao entendi. Pode repetir?")

# View principal para página do chatbot
def chatbot_view(request):
    return render(request, 'chatbot.html')

# View para receber a mensagem via AJAX
def chatbot_api(request):
    if request.method == "GET":
        user_message = request.GET.get("message")
        response = chatbot_response(user_message)
        return JsonResponse({"response": response})

