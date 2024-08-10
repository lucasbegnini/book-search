from django.test import TestCase
from io import BytesIO
from booksearch.models import Book
from booksearch.controllers.books_controller import process_csv_file
from booksearch.serializers.csv_upload_serializer import CSVUploadSerializer


class ProcessCSVFileTest(TestCase):
    def test_process_csv_file(self):
        # Create a sample CSV file
        csv_data = "Ym9va19pZCxnb29kcmVhZHNfYm9va19pZCxiZXN0X2Jvb2tfaWQsd29ya19pZCxib29rc19jb3VudCxpc2JuLGlzYm4xMyxhdXRob3JzLG9yaWdpbmFsX3B1YmxpY2F0aW9uX3llYXIsb3JpZ2luYWxfdGl0bGUsdGl0bGUsbGFuZ3VhZ2VfY29kZSxhdmVyYWdlX3JhdGluZyxyYXRpbmdzX2NvdW50LHdvcmtfcmF0aW5nc19jb3VudCx3b3JrX3RleHRfcmV2aWV3c19jb3VudCxyYXRpbmdzXzEscmF0aW5nc18yLHJhdGluZ3NfMyxyYXRpbmdzXzQscmF0aW5nc181LGltYWdlX3VybCxzbWFsbF9pbWFnZV91cmwNCjEsMjc2NzA1MiwyNzY3MDUyLDI3OTI3NzUsMjcyLDQzOTAyMzQ4MywiOSw3OEUrMjMiLFN1emFubmUgQ29sbGlucywyMDA4LjAsVGhlIEh1bmdlciBHYW1lcywiVGhlIEh1bmdlciBHYW1lcyAoVGhlIEh1bmdlciBHYW1lcywgIzEpIixlbmcsNC4zNCw0NzgwNjUzLDQ5NDIzNjUsMTU1MjU0LDY2NzE1LDEyNzkzNiw1NjAwOTIsMTQ4MTMwNSwyNzA2MzE3LGh0dHBzOi8vaW1hZ2VzLmdyLWFzc2V0cy5jb20vYm9va3MvMTQ0NzMwMzYwM20vMjc2NzA1Mi5qcGcsaHR0cHM6Ly9pbWFnZXMuZ3ItYXNzZXRzLmNvbS9ib29rcy8xNDQ3MzAzNjAzcy8yNzY3MDUyLmpwZw0KMiwzLDMsNDY0MDc5OSw0OTEsNDM5NTU0OTM0LCI5LDc4RSsyMyIsIkouSy4gUm93bGluZywgTWFyeSBHcmFuZFByw6kiLDE5OTcuMCxIYXJyeSBQb3R0ZXIgYW5kIHRoZSBQaGlsb3NvcGhlcidzIFN0b25lLCJIYXJyeSBQb3R0ZXIgYW5kIHRoZSBTb3JjZXJlcidzIFN0b25lIChIYXJyeSBQb3R0ZXIsICMxKSIsZW5nLDQuNDQsNDYwMjQ3OSw0ODAwMDY1LDc1ODY3LDc1NTA0LDEwMTY3Niw0NTUwMjQsMTE1NjMxOCwzMDExNTQzLGh0dHBzOi8vaW1hZ2VzLmdyLWFzc2V0cy5jb20vYm9va3MvMTQ3NDE1NDAyMm0vMy5qcGcsaHR0cHM6Ly9pbWFnZXMuZ3ItYXNzZXRzLmNvbS9ib29rcy8xNDc0MTU0MDIycy8zLmpwZw0KMyw0MTg2NSw0MTg2NSwzMjEyMjU4LDIyNiwzMTYwMTU4NDksIjksNzhFKzIzIixTdGVwaGVuaWUgTWV5ZXIsMjAwNS4wLFR3aWxpZ2h0LCJUd2lsaWdodCAoVHdpbGlnaHQsICMxKSIsZW4tVVMsMy41NywzODY2ODM5LDM5MTY4MjQsOTUwMDksNDU2MTkxLDQzNjgwMiw3OTMzMTksODc1MDczLDEzNTU0MzksaHR0cHM6Ly9pbWFnZXMuZ3ItYXNzZXRzLmNvbS9ib29rcy8xMzYxMDM5NDQzbS80MTg2NS5qcGcsaHR0cHM6Ly9pbWFnZXMuZ3ItYXNzZXRzLmNvbS9ib29rcy8xMzYxMDM5NDQzcy80MTg2NS5qcGcNCjQsMjY1NywyNjU3LDMyNzU3OTQsNDg3LDYxMTIwMDgxLCI5LDc4RSsyMyIsSGFycGVyIExlZSwxOTYwLjAsVG8gS2lsbCBhIE1vY2tpbmdiaXJkLFRvIEtpbGwgYSBNb2NraW5nYmlyZCxlbmcsNC4yNSwzMTk4NjcxLDMzNDA4OTYsNzI1ODYsNjA0MjcsMTE3NDE1LDQ0NjgzNSwxMDAxOTUyLDE3MTQyNjcsaHR0cHM6Ly9pbWFnZXMuZ3ItYXNzZXRzLmNvbS9ib29rcy8xMzYxOTc1NjgwbS8yNjU3LmpwZyxodHRwczovL2ltYWdlcy5nci1hc3NldHMuY29tL2Jvb2tzLzEzNjE5NzU2ODBzLzI2NTcuanBnDQo1LDQ2NzEsNDY3MSwyNDU0OTQsMTM1Niw3NDMyNzM1NjcsIjksNzhFKzIzIixGLiBTY290dCBGaXR6Z2VyYWxkLDE5MjUuMCxUaGUgR3JlYXQgR2F0c2J5LFRoZSBHcmVhdCBHYXRzYnksZW5nLDMuODksMjY4MzY2NCwyNzczNzQ1LDUxOTkyLDg2MjM2LDE5NzYyMSw2MDYxNTgsOTM2MDEyLDk0NzcxOCxodHRwczovL2ltYWdlcy5nci1hc3NldHMuY29tL2Jvb2tzLzE0OTA1Mjg1NjBtLzQ2NzEuanBnLGh0dHBzOi8vaW1hZ2VzLmdyLWFzc2V0cy5jb20vYm9va3MvMTQ5MDUyODU2MHMvNDY3MS5qcGc="
        serializer = CSVUploadSerializer(data=csv_data)

        # Call the function
        if serializer.is_valid():
            process_csv_file(serializer.validated_data["csv_file"])

            # Check if the book was created
            book = Book.objects.get(book_id=1)
            self.assertEqual(book.goodreads_book_id, "123")
            self.assertEqual(book.best_book_id, "456")
            self.assertEqual(book.work_id, "789")
            self.assertEqual(book.books_count, "10")
            self.assertEqual(book.isbn, "1234567890")
            self.assertEqual(book.isbn13, "1234567890123")
            self.assertEqual(book.authors, "John Doe")
            self.assertEqual(book.original_publication_year, "2022")
            self.assertEqual(book.original_title, "Test Book")
