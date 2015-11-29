from rest_framework import viewsets, filters
from serializers import ReceitaListSerializer, ReceitaDetailSerializer, CategoriaSerializer
from models import Receita, Categoria

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class ReceitaList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def valida_categoria(self, data):
        nome_categoria = data['categoria']
        Categoria.objects.get_or_create(nome=nome_categoria)

    def get(self, request, format=None):
        receita = Receita.objects.all()
        serializer = ReceitaListSerializer(receita, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        self.valida_categoria(request.data)
        serializer = ReceitaDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Receita.objects.get(pk=pk)
        except Receita.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        receita = self.get_object(pk)
        serializer = ReceitaDetailSerializer(receita)
        return Response(serializer.data)


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que categorias sejam vistas e editadas.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('nome',)

