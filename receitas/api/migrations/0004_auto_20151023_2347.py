# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_receita'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='title',
            new_name='autor',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='code',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='language',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='style',
        ),
        migrations.AddField(
            model_name='receita',
            name='estrelas',
            field=models.DecimalField(default=1, max_digits=1, decimal_places=0),
        ),
        migrations.AddField(
            model_name='receita',
            name='ingredientes',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='receita',
            name='nome',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='receita',
            name='preparo',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='receita',
            name='rendimento',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='receita',
            name='tempo',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
