# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171203_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
