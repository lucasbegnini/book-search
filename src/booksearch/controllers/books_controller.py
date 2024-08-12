from io import StringIO
import csv
import logging
from booksearch.models import Book


def process_csv_file(decoded_file):
    try:
        decoded_file_str = decoded_file.decode("utf-8")
        csv_file = StringIO(decoded_file_str)
        reader = csv.DictReader(csv_file)
    except Exception as e:
        logging.error(f"Error processing CSV file: {e}")
        raise Exception("Error processing CSV file")

    try:
        books_to_create = []
        books_to_update = []
        for row in reader:
            isbn13_value = row.get("isbn13", "")
            # Verifica se o valor está em notação científica e converte para string
            if isinstance(isbn13_value, float):
                isbn13_value = f"{isbn13_value:.0f}"  # Remove a notação científica
            elif isinstance(isbn13_value, str) and "e" in isbn13_value.lower():
                isbn13_value = f"{float(isbn13_value):.0f}"

            book_id = int(row["book_id"])
            existing_book = Book.objects.filter(book_id=book_id).first()

            if existing_book:
                # Atualizar os campos do livro existente
                existing_book.goodreads_book_id = (
                    int(row.get("goodreads_book_id", 0))
                    if row.get("goodreads_book_id")
                    else None
                )
                existing_book.best_book_id = (
                    int(row.get("best_book_id", 0)) if row.get("best_book_id") else None
                )
                existing_book.work_id = (
                    int(row.get("work_id", 0)) if row.get("work_id") else None
                )
                existing_book.books_count = (
                    int(row.get("books_count", 0)) if row.get("books_count") else None
                )
                existing_book.isbn = row.get("isbn")
                existing_book.isbn13 = isbn13_value
                existing_book.authors = row.get("authors")
                existing_book.original_publication_year = (
                    int(float(row.get("original_publication_year", 0)))
                    if row.get("original_publication_year")
                    else None
                )
                existing_book.original_title = row.get("original_title")
                existing_book.title = row.get("title")
                existing_book.language_code = row.get("language_code")
                existing_book.average_rating = (
                    float(row.get("average_rating", 0.0))
                    if row.get("average_rating")
                    else None
                )
                existing_book.ratings_count = (
                    int(row.get("ratings_count", 0))
                    if row.get("ratings_count")
                    else None
                )
                existing_book.work_ratings_count = (
                    int(row.get("work_ratings_count", 0))
                    if row.get("work_ratings_count")
                    else None
                )
                existing_book.work_text_reviews_count = (
                    int(row.get("work_text_reviews_count", 0))
                    if row.get("work_text_reviews_count")
                    else None
                )
                existing_book.ratings_1 = (
                    int(row.get("ratings_1", 0)) if row.get("ratings_1") else None
                )
                existing_book.ratings_2 = (
                    int(row.get("ratings_2", 0)) if row.get("ratings_2") else None
                )
                existing_book.ratings_3 = (
                    int(row.get("ratings_3", 0)) if row.get("ratings_3") else None
                )
                existing_book.ratings_4 = (
                    int(row.get("ratings_4", 0)) if row.get("ratings_4") else None
                )
                existing_book.ratings_5 = (
                    int(row.get("ratings_5", 0)) if row.get("ratings_5") else None
                )
                existing_book.image_url = row.get("image_url")
                existing_book.small_image_url = row.get("small_image_url")
                books_to_update.append(existing_book)
            else:
                book = Book(
                    book_id=book_id,
                    goodreads_book_id=(
                        int(row.get("goodreads_book_id", 0))
                        if row.get("goodreads_book_id")
                        else None
                    ),
                    best_book_id=(
                        int(row.get("best_book_id", 0))
                        if row.get("best_book_id")
                        else None
                    ),
                    work_id=int(row.get("work_id", 0)) if row.get("work_id") else None,
                    books_count=(
                        int(row.get("books_count", 0))
                        if row.get("books_count")
                        else None
                    ),
                    isbn=row.get("isbn"),
                    isbn13=isbn13_value,
                    authors=row.get("authors"),
                    original_publication_year=(
                        int(float(row.get("original_publication_year", 0)))
                        if row.get("original_publication_year")
                        else None
                    ),
                    original_title=row.get("original_title"),
                    title=row.get("title"),
                    language_code=row.get("language_code"),
                    average_rating=(
                        float(row.get("average_rating", 0.0))
                        if row.get("average_rating")
                        else None
                    ),
                    ratings_count=(
                        int(row.get("ratings_count", 0))
                        if row.get("ratings_count")
                        else None
                    ),
                    work_ratings_count=(
                        int(row.get("work_ratings_count", 0))
                        if row.get("work_ratings_count")
                        else None
                    ),
                    work_text_reviews_count=(
                        int(row.get("work_text_reviews_count", 0))
                        if row.get("work_text_reviews_count")
                        else None
                    ),
                    ratings_1=(
                        int(row.get("ratings_1", 0)) if row.get("ratings_1") else None
                    ),
                    ratings_2=(
                        int(row.get("ratings_2", 0)) if row.get("ratings_2") else None
                    ),
                    ratings_3=(
                        int(row.get("ratings_3", 0)) if row.get("ratings_3") else None
                    ),
                    ratings_4=(
                        int(row.get("ratings_4", 0)) if row.get("ratings_4") else None
                    ),
                    ratings_5=(
                        int(row.get("ratings_5", 0)) if row.get("ratings_5") else None
                    ),
                    image_url=row.get("image_url"),
                    small_image_url=row.get("small_image_url"),
                )
                books_to_create.append(book)

        # Bulk update and create
        Book.objects.bulk_update(
            books_to_update,
            [
                "goodreads_book_id",
                "best_book_id",
                "work_id",
                "books_count",
                "isbn",
                "isbn13",
                "authors",
                "original_publication_year",
                "original_title",
                "title",
                "language_code",
                "average_rating",
                "ratings_count",
                "work_ratings_count",
                "work_text_reviews_count",
                "ratings_1",
                "ratings_2",
                "ratings_3",
                "ratings_4",
                "ratings_5",
                "image_url",
                "small_image_url",
            ],
        )
        Book.objects.bulk_create(books_to_create)
    except Exception as e:
        logging.error(f"Error processing books: {e}")
        raise Exception("Error processing books")
