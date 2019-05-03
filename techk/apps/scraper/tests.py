# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Category
from .usecases import scrapy

# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Test Category')

    def test_category_created_successfully(self):
        category = Category.objects.get(name="Test Category").name
        self.assertEqual(category, 'Test Category')


class ScrapyTestCase(TestCase):
    def setUp(self):
        scrapy()

    def test_categories_save_successfully(self):
        category = Category.objects.get(id='6').name
        self.assertEqual(category, 'Philosophy')
