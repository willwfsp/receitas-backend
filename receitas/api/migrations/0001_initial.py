# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('nome', models.CharField(default=b'', max_length=100, serialize=False, primary_key=True, blank=True)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, blank=True)),
                ('quantidade', models.IntegerField(default=1, blank=True)),
                ('unidade', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Metodo',
            fields=[
                ('nome', models.CharField(default=b'', max_length=100, serialize=False, primary_key=True, blank=True)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, blank=True)),
                ('descricao', models.CharField(max_length=300, blank=True)),
                ('foto', models.CharField(default=b'', max_length=200, blank=True)),
                ('tempo', models.IntegerField(default=1, blank=True)),
                ('rendimento', models.IntegerField(default=1, blank=True)),
                ('valor_nutricional', models.IntegerField(default=1, blank=True)),
                ('estrelas', models.IntegerField(default=1, blank=True)),
                ('instrucoes', models.CharField(max_length=800, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(related_name='receitas', to='api.Categoria')),
                ('metodo', models.ForeignKey(related_name='receitas', to='api.Metodo')),
                ('owner', models.ForeignKey(related_name='receitas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='receita',
            field=models.ForeignKey(related_name='ingredientes', to='api.Receita'),
        ),
    ]
