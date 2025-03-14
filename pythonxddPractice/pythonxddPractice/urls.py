# pythonxddPractice/urls.py

from django.contrib import admin
from django.urls import path, include  # <--- Importante: incluir "include"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja.urls')),  # <--- Incluindo as rotas do app loja
]
