# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.db import models
from .serializers import CategorySerializer, BookSerializer

from .usecases import scrapy
from .models import Category, Book

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ajax(request):
    #scrapy()
    book = Category.objects.all()
    serializer = CategorySerializer(book, many=True)
    return JsonResponse(serializer.data, safe=False)
