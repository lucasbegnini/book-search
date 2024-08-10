from rest_framework import serializers
from booksearch.models.book_models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "original_title", "authors", "isbn"]
