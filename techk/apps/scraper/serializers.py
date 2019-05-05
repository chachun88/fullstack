from rest_framework import serializers
from .models import Category, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    book = BookSerializer(source="book_set", read_only=True, many=True)
    class Meta:
       model = Category
       fields = ("name", "book",)
