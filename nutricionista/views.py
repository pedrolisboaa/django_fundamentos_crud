from django.shortcuts import render
from django.template.context_processors import request

from .models import Nutricionista
from .form import PacienteForm

# Create your views here.


def listar_paciente(request):
    # É Criado uma váriavel que recebe todos os pacientes do banco
    pacientes = Nutricionista.objects.all()
    return render(request, 'nutricionista/listar_pacientes.html', {'pacientes': pacientes})


def inserir_paciente(request):
    # Para inserir um cliente é necessário verificar que o request é do metodo POST, caso ele seja criar uma
    # instancia do formulário, se ele for válido salvar. Caso não seja será gerada uma istáncia vazia do formulário.
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PacienteForm()
    return render(request, 'nutricionista/form_paciente.html', {'form': form})





