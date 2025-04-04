# Generated by Django 4.1 on 2025-03-09 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagem', models.CharField(blank=True, max_length=300, null=True)),
                ('link_pagamento', models.URLField(blank=True, max_length=300, null=True)),
                ('destaque', models.BooleanField(default=False)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoria')),
                ('cidades', models.ManyToManyField(blank=True, to='location.cidade')),
            ],
        ),
    ]
