__author__ = 'Willian'
from django.db import models

class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100, blank=True, default='')
    foto = models.CharField(max_length=200, blank=True, default='')
    estrelas = models.IntegerField(blank=True, default=1)


    class Meta:
        ordering = ('created',)

