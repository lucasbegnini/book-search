from django.db import models

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    goodreads_book_id = models.IntegerField(null=True, blank=True)
    best_book_id = models.IntegerField(null=True, blank=True)
    work_id = models.IntegerField(null=True, blank=True)
    books_count = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    isbn13 = models.CharField(max_length=13, null=True, blank=True)
    authors = models.CharField(max_length=255, null=True, blank=True)
    original_publication_year = models.IntegerField(null=True, blank=True)
    original_title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.original_title} by {self.authors}'

    class Meta:
        db_table = 'books'
        ordering = ['original_publication_year']