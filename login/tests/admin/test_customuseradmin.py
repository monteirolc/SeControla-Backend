import pytest
from django.contrib import admin
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model
from login.models import CustomUser
from login.admin import CustomUserAdmin

User = get_user_model()


@pytest.mark.django_db
class TestCustomUserAdmin:
    def test_customuser_is_registered_in_admin(self):
        # Garante que o CustomUser está registrado no admin
        assert CustomUser in admin.site._registry
        assert isinstance(admin.site._registry[CustomUser], CustomUserAdmin)

    def test_list_display_fields(self):
        customuser_admin = admin.site._registry[CustomUser]
        expected = (
            "username", "name", "last_name", "email", "cpf", "phone",
            "age", "is_staff", "is_active"
        )
        assert customuser_admin.list_display == expected

    def test_search_fields(self):
        customuser_admin = admin.site._registry[CustomUser]
        expected = ("username", "email", "cpf", "name", "last_name")
        assert customuser_admin.search_fields == expected

    def test_ordering(self):
        customuser_admin = admin.site._registry[CustomUser]
        assert customuser_admin.ordering == ("username",)

    def test_admin_login_and_access_changelist(self, django_user_model):
        # Criar superusuário para acessar admin
        admin_user = django_user_model.objects.create_superuser(
            username="admin",
            password="admin123",
            name="Admin",
            last_name="Root",
            email="admin@example.com",
            cpf="12345678901"
        )
        client = Client()
        client.force_login(admin_user)

        url = reverse("admin:login_customuser_changelist")
        response = client.get(url)

        assert response.status_code == 200
        assert "Custom user" in response.content.decode().lower()
