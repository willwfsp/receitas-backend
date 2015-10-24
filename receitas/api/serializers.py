from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Receita


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ('id', 'nome', 'estrelas', 'tempo', 'autor', 'rendimento', 'ingredientes', 'preparo')
