__author__ = 'Willian'
from django.db import models

class Receita(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100, blank=True, default='')
    rendimento = models.CharField(max_length=100, blank=True, default='')
    estrelas = models.IntegerField(blank=True, default=1)
    tempo = models.CharField(verbose_name='tempo em minutos', max_length=100, blank=True, default='')
    autor = models.ForeignKey('Usuario', verbose_name='autor da receita')
    categoria = models.ForeignKey('Categoria', verbose_name='categoria da receita')
    galeria = models.ManyToManyField('Imagem', verbose_name='lista de imagens da receita', related_name='receita_imagem')
    comentarios = models.ManyToManyField('Comentario', verbose_name='lista de comentarios da receita')
    partes = models.ManyToManyField('Parte', verbose_name='lista de partes da receita')

    class Meta:
        ordering = ('created',)


class Usuario(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    senha = models.CharField(max_length=100, blank=True, default='')
    receitas = models.ManyToManyField('Receita', verbose_name='lista de receitas')

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return '%s' % self.nome


class Categoria(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100, blank=True, default='')
    receitas = models.ManyToManyField('Receita', verbose_name='lista de receitas', related_name='receita_categoria')

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return '%s' % self.nome


class Imagem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    legenda = models.CharField(max_length=100, blank=True, default='')
    src = models.CharField(max_length=100, blank=True, default='')
    receita = models.ForeignKey('Receita', verbose_name='receita correspondente')

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return '%s' % self.legenda


class Comentario(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey('Usuario', verbose_name='autor do comentario')
    texto = models.CharField(max_length=280, blank=True, default='')
    estrelas = models.IntegerField(blank=True, default=1)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return '%s, %s, %s estrelas' % (self.usuario, self.texto, self.estrelas)


class Parte(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=50, blank=True, default='')
    preparo = models.ManyToManyField('Passo', verbose_name='passo do preparo de uma parte', related_name='parte_passo')
    ingredientes = models.ManyToManyField('Ingrediente', verbose_name='ingreditentes de uma parte', related_name='parte_ingrediente')

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return '%s' % self.nome


class Passo(models.Model):

    descricao = models.CharField(max_length=100, blank=True, default='')
    parte = models.ForeignKey('Parte', verbose_name='parte da receita')

    class Meta:
        ordering = ('descricao',)

    def __unicode__(self):
        return '%s' % self.descricao


class Ingrediente(models.Model):

    nome = models.CharField(max_length=50, blank=True, default='')
    mdedida = models.CharField(max_length=50, blank=True, default='')
    quantidade = models.DecimalField(max_digits=5, decimal_places=1)
    parte = models.ForeignKey('Parte', verbose_name='parte da receita')

    class Meta:
        ordering = ('nome',)

    def __unicode__(self):
        return '%s' % self.nome
