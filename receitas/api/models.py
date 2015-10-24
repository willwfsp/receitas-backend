__author__ = 'Willian'
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Receita(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100, blank=True, default='')
    estrelas = models.IntegerField(blank=True, default=1)
    tempo = models.CharField(max_length=100, blank=True, default='')
    rendimento = models.CharField(max_length=100, blank=True, default='')
    ingredientes = models.CharField(max_length=100, blank=True, default='')
    autor = models.CharField(max_length=100, blank=True, default='')
    preparo = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)