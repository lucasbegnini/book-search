from django.db import models


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    goodreads_book_id = models.IntegerField(null=True, blank=True)
    best_book_id = models.IntegerField(null=True, blank=True)
    work_id = models.IntegerField(null=True, blank=True)
    books_count = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(
        max_length=13, null=True, blank=True
    )  # CharField para ISBN com letras
    isbn13 = models.CharField(
        max_length=13, null=True, blank=True
    )  # CharField para ISBN13
    authors = models.CharField(max_length=255, null=True, blank=True)
    original_publication_year = models.IntegerField(null=True, blank=True)
    original_title = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    language_code = models.CharField(max_length=10, null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    ratings_count = models.IntegerField(null=True, blank=True)
    work_ratings_count = models.IntegerField(null=True, blank=True)
    work_text_reviews_count = models.IntegerField(null=True, blank=True)
    ratings_1 = models.IntegerField(null=True, blank=True)
    ratings_2 = models.IntegerField(null=True, blank=True)
    ratings_3 = models.IntegerField(null=True, blank=True)
    ratings_4 = models.IntegerField(null=True, blank=True)
    ratings_5 = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=200, null=True, blank=True)
    small_image_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.authors}"

    class Meta:
        db_table = "books"
        ordering = ["original_publication_year"]
