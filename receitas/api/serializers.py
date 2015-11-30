from rest_framework import serializers
from models import Receita, Categoria, Ingrediente, Metodo

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    receitas = serializers.PrimaryKeyRelatedField(many=True, queryset=Receita.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'receitas')


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('nome', 'quantidade', 'unidade')


class ReceitaListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Receita
        fields = ('id', 'nome', 'estrelas', 'foto', 'categoria', 'owner')


class ReceitaDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    ingredientes = IngredienteSerializer(many=True)

    class Meta:
        model = Receita
        fields = ('id', 'nome', 'estrelas', 'foto', 'categoria', 'valor_nutricional', 'rendimento', 'tempo', 'descricao',
        'ingredientes', 'metodo', 'instrucoes','owner')

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
