from booksearch.models.book_models import Book
from booksearch.serializers.book_serializer import BookSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "book_id",
        "goodreads_book_id",
        "isbn",
        "isbn13",
        "authors",
        "original_publication_year",
        "language_code",
        "average_rating",
        "title",
    ]

    search_fields = ["title", "authors", "isbn", "isbn13", "original_title"]
