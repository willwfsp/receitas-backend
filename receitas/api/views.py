from rest_framework import viewsets, filters, generics
from serializers import ReceitaListSerializer, ReceitaDetailSerializer, CategoriaSerializer, UserSerializer,UserPOSTSerializer
from models import Receita, Categoria, Metodo
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
from permissions import IsOwnerOrReadOnly
from rest_framework import permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserPOSTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReceitaList(APIView):
    """
    Lista todas as receitas resumidamente ou cria uma receita completa
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Receita.objects.all()
    serializer_class = ReceitaListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('nome',)

    def valida_categoria(self, data):
        if 'categoria' in data:
            nome_categoria = data['categoria']
            Categoria.objects.get_or_create(nome=nome_categoria)

    def valida_metodo(self, data):
        print(data)
        if 'metodo' in data:
            nome_metodo = data['metodo']
            Metodo.objects.get_or_create(nome=nome_metodo)

    @csrf_exempt
    def get(self, request, format=None):
        receita = Receita.objects.all()
        serializer = ReceitaListSerializer(receita, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        self.valida_categoria(request.data)
        self.valida_metodo(request.data)
        serializer = ReceitaDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReceitaDetail(APIView):
    """
    Recupera, atualiza ou deleta instancias de receitas.
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def valida_categoria(self, data):
        if 'categoria' in data:
            nome_categoria = data['categoria']
            Categoria.objects.get_or_create(nome=nome_categoria)

    def valida_metodo(self, data):
        print(data)
        if 'metodo' in data:
            nome_metodo = data['metodo']
            Metodo.objects.get_or_create(nome=nome_metodo)

    def get_object(self, pk):
        try:
            return Receita.objects.get(pk=pk)
        except Receita.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        receita = self.get_object(pk)
        serializer = ReceitaDetailSerializer(receita)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        self.valida_categoria(request.data)
        self.valida_metodo(request.data)
        receita = self.get_object(pk)
        serializer = ReceitaDetailSerializer(receita, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que categorias sejam vistas e editadas.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('nome',)


