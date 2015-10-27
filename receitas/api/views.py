from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters, generics
from serializers import ReceitasSerializer, UsuariosSerializer, PassosSerializer, PartesSerializer, \
    IngredientesSerializer
from models import Receita, Usuario, Passo, Parte, Ingrediente


class ReceitaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que receitas sejam vistas e editadas.
    """
    queryset = Receita.objects.all()
    serializer_class = ReceitasSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('autor', 'estrelas')


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que receitas sejam vistas e editadas.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class ParteViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que receitas sejam vistas e editadas.
    """
    queryset = Parte.objects.all()
    serializer_class = PartesSerializer


class PassoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que receitas sejam vistas e editadas.
    """
    queryset = Passo.objects.all()
    serializer_class = PassosSerializer


class IngredienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que receitas sejam vistas e editadas.
    """
    queryset = Ingrediente.objects.all()
    serializer_class = IngredientesSerializer
