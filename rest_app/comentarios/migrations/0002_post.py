# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, verbose_name=b'Usuario')),
                ('conteudo', models.CharField(max_length=140, verbose_name=b'Conteudo')),
            ],
        ),
    ]
