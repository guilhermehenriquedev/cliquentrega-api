from django.contrib import admin
from .models import Cidade

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado', 'valor', 'label')
    search_fields = ('nome', 'estado', 'label')
    list_filter = ('estado',)
    ordering = ('nome',)
