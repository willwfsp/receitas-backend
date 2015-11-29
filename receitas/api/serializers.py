from rest_framework import serializers
from models import Receita, Categoria, Ingrediente, Metodo


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('nome', 'quantidade', 'unidade')


class ReceitaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receita
        fields = ('id', 'nome', 'estrelas', 'foto', 'categoria')


class ReceitaDetailSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True)

    class Meta:
        model = Receita
        fields = ('id', 'nome', 'estrelas', 'foto', 'categoria', 'valor_nutricional', 'rendimento', 'tempo', 'descricao',
        'ingredientes', 'metodo', 'instrucoes')

    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingredientes')
        receita = Receita.objects.create(**validated_data)
        for ingrediente_data in ingredientes_data:
            Ingrediente.objects.create(receita=receita, **ingrediente_data)
        return receita


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nome',)

class MetodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodo
        fields = ('nome',)
