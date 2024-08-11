from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group, Permission


class UserCreateViewTest(APITestCase):
    def setUp(self):
        group_name = "Regular Users"
        if not Group.objects.filter(name=group_name).exists():
            group = Group.objects.create(name=group_name)
            permissions = Permission.objects.filter(codename__in=["can view book"])
            group.permissions.add(*permissions)

    def test_create_user(self):
        url = reverse("user-register")
        data = {
            "username": "novo_usuario",
            "password": "senha_segura123",
            "email": "novo_usuario@example.com",
            "first_name": "Nome",
            "last_name": "Sobrenome",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "novo_usuario")
