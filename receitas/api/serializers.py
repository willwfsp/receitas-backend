from rest_framework import serializers
from models import Receita, Categoria


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ('id', 'nome', 'estrelas', 'foto', 'categoria')

    def create(self, validated_data):
        nome_categoria = validated_data.pop('categoria')

        categoria = Categoria.objects.get_or_create(nome=nome_categoria)
        print(str(categoria))
        receita = Receita.objects.create(categoria=categoria, **validated_data)
        return receita

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('nome',)
