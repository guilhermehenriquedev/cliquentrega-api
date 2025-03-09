from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    search_fields = ('nome',)
    prepopulated_fields = {"slug": ("nome",)}
    ordering = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria', 'destaque')
    search_fields = ('nome', 'categoria__nome')
    list_filter = ('categoria', 'destaque', 'cidades')
    ordering = ('nome',)
    filter_horizontal = ('cidades',)
