from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from booksearch.serializers.csv_upload_serializer import CSVUploadSerializer
from booksearch.controllers.books_controller import process_csv_file
from rest_framework import status


class CSVView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CSVUploadSerializer(data=request.data)
        if serializer.is_valid():
            try:
                process_csv_file(serializer.validated_data["csv_file"])
            except Exception as e:
                return Response({"status": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"status": "CSV file processed successfully."})
