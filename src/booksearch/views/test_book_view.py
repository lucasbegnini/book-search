from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from booksearch.models.book_models import Book
from booksearch.serializers.book_serializer import BookSerializer


class BookModel(TestCase):
    def setUp(self):
        # Criação de uma instância de Book para os testes
        self.book = Book.objects.create(
            book_id=1,
            goodreads_book_id=2767052,
            best_book_id=2767052,
            work_id=2792775,
            books_count=272,
            isbn="043965548X",
            isbn13="9780439655484",
            authors="Suzanne Collins",
            original_publication_year=2008,
            original_title="The Hunger Games",
            title="The Hunger Games",
            language_code="en",
            average_rating=4.34,
            ratings_count=2000,
            work_ratings_count=1000,
            work_text_reviews_count=200,
            ratings_1=150,
            ratings_2=500,
            ratings_3=250,
            ratings_4=500,
            ratings_5=500,
            image_url="http://example.com/image.jpg",
            small_image_url="http://example.com/small_image.jpg",
        )

    def test_book_creation(self):
        # Verifica se a instância de Book foi criada corretamente
        self.assertIsInstance(self.book, Book)

    def test_book_string_representation(self):
        # Verifica se a representação em string do Book é conforme esperado
        self.assertEqual(str(self.book), "The Hunger Games by Suzanne Collins")

    def test_default_ordering(self):
        # Testa se o ordering padrão é por 'original_publication_year'
        books = Book.objects.all()
        self.assertEqual(books[0].original_publication_year, 2008)


class BookViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_id = 2
        self.book_data = {
            "book_id": self.book_id,
            "goodreads_book_id": 3,
            "best_book_id": 3,
            "work_id": 4640799,
            "books_count": 491,
            "isbn": "439554934",
            "isbn13": "9780439554930",
            "authors": "J.K. Rowling, Mary GrandPré",
            "original_publication_year": 1997,
            "original_title": "Harry Potter and the Philosopher's Stone",
            "title": "Harry Potter and the Sorcerer's Stone (Harry Potter, #1)",
            "language_code": "eng",
            "average_rating": 4.44,
            "ratings_count": 4602479,
            "work_ratings_count": 4800065,
            "work_text_reviews_count": 75867,
            "ratings_1": 75504,
            "ratings_2": 101676,
            "ratings_3": 455024,
            "ratings_4": 1156318,
            "ratings_5": 3011543,
            "image_url": "https://images.gr-assets.com/books/1474154022m/3.jpg",
            "small_image_url": "https://images.gr-assets.com/books/1474154022s/3.jpg",
        }

    def test_create_book(self):
        url = reverse("book-list")
        response = self.client.post(url, self.book_data, format="json")
        self.assertEqual(response.json(), self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
