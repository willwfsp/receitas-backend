# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
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
                ('created', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(related_name='receitas', to='api.Categoria')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
