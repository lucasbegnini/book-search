from rest_framework import serializers
import base64


class CSVUploadSerializer(serializers.Serializer):

    csv_file = serializers.CharField(required=True)

    def validate_csv_file(self, value):
        try:
            # Decodificar a string base64
            decoded_file = base64.b64decode(value)
            return decoded_file
        except Exception as e:
            raise serializers.ValidationError("Arquivo base64 inválido.")
