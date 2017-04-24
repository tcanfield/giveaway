# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 02:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Giveaway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField(default=datetime.datetime.now)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('odds', models.DecimalField(decimal_places=999, max_digits=999)),
                ('winner_email_address', models.EmailField(max_length=254)),
                ('attempts', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('referral_link', models.URLField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=999)),
            ],
        ),
        migrations.AddField(
            model_name='giveaway',
            name='prize',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.Prize'),
        ),
    ]
