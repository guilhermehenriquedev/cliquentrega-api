from rest_framework import serializers
from .models import Produto, Categoria, Cidade, Flag
from cliquentrega_app.location.serializers import CidadeSerializer


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flag
        fields = '__all__'
        
class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), source='categoria', write_only=True
    )
    cidades = CidadeSerializer(many=True, read_only=True)
    cidades_ids = serializers.PrimaryKeyRelatedField(
        queryset=Cidade.objects.all(), many=True, source='cidades', write_only=True
    )
    flag = FlagSerializer(read_only=True, allow_null=True)
    flag_id = serializers.PrimaryKeyRelatedField(
        queryset=Flag.objects.all(), source='flag', write_only=True, allow_null=True
    )
    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'preco', 'categoria', 'categoria_id', 'flag', 'flag_id',
            'imagem', 'cidades', 'cidades_ids', 'link_pagamento', 'destaque', 'descricao'
        ]