__author__ = 'Willian'
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, blank=True, default='', primary_key=True)

    class Meta:
        ordering = ('nome',)

    def __unicode__(self):
        return '%s' % self.nome

class Receita(models.Model):

    nome = models.CharField(max_length=50, blank=True)
    descricao = models.CharField(max_length=300, blank=True)
    foto = models.CharField(max_length=200, blank=True, default='')
    categoria = models.ForeignKey(Categoria, related_name='receitas')
    tempo = models.IntegerField(blank=True, default=1)
    rendimento = models.IntegerField(blank=True, default=1)
    valor_nutricional = models.IntegerField(blank=True, default=1)
    estrelas = models.IntegerField(blank=True, default=1)

    #ingredientes
    #instrucoes
    #metodo cozimento

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)




