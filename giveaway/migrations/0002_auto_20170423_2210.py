# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prize',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=999),
        ),
    ]
