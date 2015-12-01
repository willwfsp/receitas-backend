# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, blank=True)),
                ('user', models.OneToOneField(related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
