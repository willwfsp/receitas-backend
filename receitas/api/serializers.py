from rest_framework import serializers
from models import Receita, Usuario, Comentario, Imagem, Parte, Passo, Categoria, Ingrediente

class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ('id', 'nome', 'estrelas', 'autor', 'rendimento', 'partes', 'categoria', 'galeria', 'comentarios')

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email')

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome')

class ImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ('id', 'legenda', 'src')


class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'usuario', 'texto', 'estrelas')

class PartesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parte
        fields = ('id', 'nome', 'preparo', 'ingredientes')

class PassosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passo
        fields = ('id', 'descricao')

class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nome', 'medida', 'quantidade')

