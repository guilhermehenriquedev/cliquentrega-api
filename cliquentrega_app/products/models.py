from django.db import models
from cliquentrega_app.location.models import Cidade


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
    
class Flag(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=10000)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE, null=True)
    imagem = models.CharField(max_length=10000, blank=True, null=True)
    cidades = models.ManyToManyField(Cidade, blank=True)
    link_pagamento = models.URLField(max_length=10000, blank=True, null=True)
    destaque = models.BooleanField(default=False)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome