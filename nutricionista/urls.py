from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listar_paciente, name='listar_paciente'),
    path('cadastrar', inserir_paciente, name='inserir_paciente'),
]
