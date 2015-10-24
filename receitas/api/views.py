from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, ReceitasSerializer
from models import Receita


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que receitas sejam vistas e editadas.
    """
    queryset = Receita.objects.all()
    serializer_class = ReceitasSerializer
