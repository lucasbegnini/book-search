from django.test import TestCase
from booksearch.models.book_models import Book


# class BookModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         Book.objects.create(
#             book_id=1,
#             goodreads_book_id=123,
#             best_book_id=456,
#             work_id=789,
#             books_count=10,
#             isbn="1234567890",
#             isbn13="1234567890123",
#             authors="John Doe",
#             original_publication_year=2022,
#             original_title="Test Book",
#         )

#     def test_str_representation(self):
#         book = Book.objects.get(book_id=1)
#         self.assertEqual(str(book), "Test Book by John Doe")

#     def test_meta_db_table(self):
#         self.assertEqual(Book._meta.db_table, "books")

#     def test_meta_ordering(self):
#         self.assertEqual(Book._meta.ordering, ["original_publication_year"])
