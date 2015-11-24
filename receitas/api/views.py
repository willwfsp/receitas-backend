from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters, generics
from serializers import RecipeSerializer
from models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que receitas sejam vistas e editadas.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('nome', 'estrelas')

