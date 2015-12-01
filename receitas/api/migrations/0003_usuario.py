# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20151130_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=200, blank=True)),
                ('nascimento', models.DateTimeField()),
                ('cidade', models.CharField(default=b'', max_length=100, blank=True)),
                ('estado', models.CharField(default=b'', max_length=2, blank=True)),
                ('telefone', models.CharField(default=b'', max_length=10, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
    ]
