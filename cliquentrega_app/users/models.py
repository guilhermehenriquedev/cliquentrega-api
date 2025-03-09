from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50, default='user')  # admin, manager, etc.

    def __str__(self):
        return self.email