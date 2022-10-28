from django.shortcuts import render
from .models import Nutricionista
from .form import PacienteForm

# Create your views here.


def listar_paciente(request):
    pacientes = Nutricionista.objects.all()
    return render(request, 'nutricionista/listar_pacientes.html', {'pacientes': pacientes})


def inserir_paciente(request):
    form = PacienteForm()
    return render(request, 'nutricionista/form_paciente.html', {'form': form})




