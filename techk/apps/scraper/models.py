# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):

  class Meta:
    app_label = 'apps.scraper'
    abstract = True

  name = models.CharField(max_length=250, unique=True)

class Book(models.Model):
     book = models.ForeignKey(Category, on_delete=models.CASCADE)
     name = models.CharField(max_length=250)
     price = models.DecimalField(max_digits=5, decimal_places=2)
     in_stock = models.IntegerField()
     valoration = models.IntegerField()
     description = models.CharField(max_length=2500)

class ExtraInformation(models.Model):
     extra_information = models.ForeignKey(Book, on_delete=models.CASCADE)
     upc = models.CharField(max_length=250)
     product_type = models.CharField(max_length=250)
     price = models.DecimalField(max_digits=5, decimal_places=2)
     price_with_tax = models.DecimalField(max_digits=5, decimal_places=2)
     tax = models.DecimalField(max_digits=5, decimal_places=2)
     availability = models.IntegerField()
     reviews = models.IntegerField()
