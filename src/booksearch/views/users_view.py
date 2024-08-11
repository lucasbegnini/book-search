from rest_framework import generics
from booksearch.serializers.user_serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
