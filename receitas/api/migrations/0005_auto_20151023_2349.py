# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20151023_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='estrelas',
            field=models.DecimalField(default=1, max_digits=1, decimal_places=1),
        ),
    ]
