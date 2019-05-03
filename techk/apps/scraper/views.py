# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

from .usecases import scrapy
from .models import Category

# Create your views here.
def index(request):
    #scrapy()
    return render(request, 'index.html')

def ajax(request):
    categories = list(Category.objects.values())
    return JsonResponse(categories, safe=False)
