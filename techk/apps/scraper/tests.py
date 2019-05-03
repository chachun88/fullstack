# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Category

# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Test Category')

    def test_category_created_successfully(self):
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category, 'The cat says "meow"')
