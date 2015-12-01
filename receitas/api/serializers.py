from rest_framework import serializers
from models import Receita, Categoria, Ingrediente, Metodo

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    receitas = serializers.PrimaryKeyRelatedField(many=True, queryset=Receita.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'receitas')


class UserPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')


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
    ingredientes = IngredienteSerializer(many=True, required=False)

    class Meta:
        model = Receita
        fields = ('id', 'nome', 'estrelas', 'foto', 'categoria', 'valor_nutricional', 'rendimento', 'tempo', 'descricao',
        'ingredientes', 'metodo', 'instrucoes','owner')

    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingredientes')
        receita = Receita.objects.create(**validated_data)
        for ingrediente_data in ingredientes_data:
            Ingrediente.objects.get_or_create(receita=receita, **ingrediente_data)
        return receita

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.estrelas = validated_data.get('estrelas', instance.estrelas)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.categoria = validated_data.get('categoria', instance.categoria)
        instance.valor_nutricional = validated_data.get('valor_nutricional', instance.valor_nutricional)
        instance.rendimento = validated_data.get('rendimento', instance.rendimento)
        instance.tempo = validated_data.get('tempo', instance.tempo)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.metodo = validated_data.get('metodo', instance.metodo)
        instance.instrucoes = validated_data.get('instrucoes', instance.instrucoes)

        Ingrediente.objects.filter(receita=instance).delete()
        ingredientes = validated_data.get('ingredientes', instance.ingredientes)

        try:
            for ingrediente in ingredientes:
                Ingrediente.objects.get_or_create(receita=instance, **ingrediente)
        except TypeError:
            print ("sem ingredientes para atualizar")

        return instance


class CategoriaSerializer(serializers.ModelSerializer):

    receitas = ReceitaListSerializer(many=True, required=False)

    class Meta:
        model = Categoria
        fields = ('nome', 'receitas')

class MetodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodo
        fields = ('nome',)
