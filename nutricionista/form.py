from django.forms import ModelForm
from .models import Nutricionista

"""
O arquivo form.py valida a regra para que o dado seja passado de forma correta para dentro do banco,
Seguindo as regras do arquivo model, ele pega todas as validações do models
"""


class PacienteForm(ModelForm):
    class Meta:
        model = Nutricionista
        fields = ['nome', 'sexo', 'peso', 'altura']
