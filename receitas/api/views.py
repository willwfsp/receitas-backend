from rest_framework import viewsets, filters
from serializers import ReceitaSerializer, CategoriaSerializer
from models import Receita, Categoria


class ReceitaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que receitas sejam vistas e editadas.
    """
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('nome', 'estrelas', 'categoria')


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que categorias sejam vistas e editadas.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('nome',)

