# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
    CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found')
    ]
    status = models.CharField(choices=CHOICES, max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=750)
    date = models.DateField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)