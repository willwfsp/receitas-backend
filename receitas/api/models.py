__author__ = 'Willian'
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, blank=True, default='', primary_key=True)

    class Meta:
        ordering = ('nome',)

    def __unicode__(self):
        return '%s' % self.nome

class Metodo(models.Model):
    nome = models.CharField(max_length=100, blank=True, default='', primary_key=True)

    class Meta:
        ordering = ('nome',)

    def __unicode__(self):
        return '%s' % self.nome

class Receita(models.Model):

    owner = models.ForeignKey('auth.User', related_name='receitas')
    nome = models.CharField(max_length=50, blank=True)
    descricao = models.CharField(max_length=300, blank=True)
    foto = models.CharField(max_length=200, blank=True, default='')
    categoria = models.ForeignKey(Categoria, blank=True, related_name='receitas')
    tempo = models.IntegerField(blank=True, default=1)
    rendimento = models.IntegerField(blank=True, default=1)
    valor_nutricional = models.IntegerField(blank=True, default=1)
    estrelas = models.IntegerField(blank=True, default=1)
    metodo = models.ForeignKey(Metodo, blank=True, related_name='receitas')
    instrucoes = models.CharField(max_length=800, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

class Ingrediente(models.Model):

    nome = models.CharField(max_length=50, blank=True)
    quantidade = models.IntegerField(blank=True, default=1)
    unidade = models.CharField(max_length=50, blank=True)
    receita = models.ForeignKey(Receita, related_name='ingredientes')

    class Meta:
        ordering = ('nome',)







