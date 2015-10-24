# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20151023_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='autor',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='receita',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='receita',
            name='estrelas',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='receita',
            name='nome',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='receita',
            name='rendimento',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='receita',
            name='tempo',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
