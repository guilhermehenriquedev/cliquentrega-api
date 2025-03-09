from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    valor = models.CharField(max_length=100)  # "sao-paulo-sp"
    label = models.CharField(max_length=100)  # "São Paulo-SP"

    def __str__(self):
        return f"{self.nome}-{self.estado}"