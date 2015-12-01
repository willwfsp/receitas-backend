# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='categoria',
            field=models.ForeignKey(related_name='receitas', blank=True, to='api.Categoria'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='metodo',
            field=models.ForeignKey(related_name='receitas', blank=True, to='api.Metodo'),
        ),
    ]
