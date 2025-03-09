from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'nome', 'cargo')
    search_fields = ('email', 'nome', 'cargo')
    list_filter = ('cargo',)
    ordering = ('nome',)
