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
        for row in reader:
            book = Book(
                book_id=row["book_id"],
                goodreads_book_id=row.get("goodreads_book_id"),
                best_book_id=row.get("best_book_id"),
                work_id=row.get("work_id"),
                books_count=row.get("books_count"),
                isbn=row.get("isbn"),
                isbn13=row.get("isbn13"),
                authors=row.get("authors"),
                original_publication_year=row.get("original_publication_year"),
                original_title=row.get("original_title"),
            )
            books_to_create.append(book)
    except Exception as e:
        logging.error(f"Error creating Book instances: {e}")
        raise Exception("Error creating Book instances")

    Book.objects.bulk_create(books_to_create)
