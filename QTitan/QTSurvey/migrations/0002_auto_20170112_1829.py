# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QTSurvey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firstName',
            field=models.CharField(default='placeholder', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(default='placeholder', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='placeholder', max_length=11),
            preserve_default=False,
        ),
    ]