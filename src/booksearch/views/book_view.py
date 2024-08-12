from booksearch.models.book_models import Book
from booksearch.serializers.book_serializer import BookSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter


class BookFilter(FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains")
    authors = CharFilter(field_name="authors", lookup_expr="icontains")
    isbn = CharFilter(field_name="isbn", lookup_expr="exact")

    class Meta:
        model = Book
        fields = {
            "book_id": ["exact"],
            "goodreads_book_id": ["exact"],
            "isbn": ["exact"],
            "isbn13": ["exact"],
            "original_publication_year": ["exact"],
            "language_code": ["exact"],
            "average_rating": ["exact"],
        }


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = BookFilter

    search_fields = ["title", "authors", "isbn", "isbn13", "original_title"]

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.query_params:
            return queryset.none()

        return queryset
