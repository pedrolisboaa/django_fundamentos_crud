from django.db import models

# Create your models here.


class Nutricionista(models.Model):
    SEXO_ESCOLHA = (
        ("F", 'Feminino'),
        ("M", 'Masculino'),
        ('N', 'Não Informar')
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_ESCOLHA, blank=False, null=False)
    peso = models.FloatField(null=False, blank=False)
    altura = models.FloatField(null=False, blank=False)

    def __string__(self):
        return self.nome
