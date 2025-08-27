import pytest
from login.serializers import UserRegisterSerializer
from login.models import CustomUser
# from django.db import IntegrityError


@pytest.mark.django_db
class TestUserRegisterSerializer:

    def test_create_user_success(self):
        data = {
            "name": "Lucas",
            "last_name": "Monteiro",
            "age": 30,
            "cpf": "12345678901",
            "email": "lucas@example.com",
            "phone": "11999999999",
            "username": "lucas123",
            "password": "strongpass"
        }
        serializer = UserRegisterSerializer(data=data)
        assert serializer.is_valid() is True
        user = serializer.save()

        # Verifica campos
        assert user.username == "lucas123"
        assert user.email == "lucas@example.com"
        assert user.cpf == "12345678901"
        # Verifica que a senha foi hashada
        assert user.check_password("strongpass") is True
        assert user.password != "strongpass"

    def test_missing_required_field(self):
        data = {
            "name": "Lucas",
            "last_name": "Monteiro",
            "age": 30,
            # "cpf" ausente
            "email": "lucas@example.com",
            "phone": "11999999999",
            "username": "lucas123",
            "password": "strongpass"
        }
        serializer = UserRegisterSerializer(data=data)
        assert serializer.is_valid() is False
        assert "cpf" in serializer.errors

    def test_duplicate_username_raises_error(self):
        CustomUser.objects.create_user(
            username="lucas123",
            password="test123",
            name="Lucas",
            last_name="Monteiro",
            email="lucas1@example.com",
            cpf="11122233344"
        )
        data = {
            "name": "Lucas",
            "last_name": "Monteiro",
            "age": 30,
            "cpf": "55566677788",
            "email": "lucas2@example.com",
            "phone": "11999999999",
            "username": "lucas123",  # duplicado
            "password": "strongpass"
        }
        serializer = UserRegisterSerializer(data=data)
        assert serializer.is_valid() is False
        assert "username" in serializer.errors

    def test_duplicate_email_raises_error(self):
        CustomUser.objects.create_user(
            username="lucas1",
            password="test123",
            name="Lucas",
            last_name="Monteiro",
            email="lucas@example.com",
            cpf="11122233344"
        )
        data = {
            "name": "Lucas",
            "last_name": "Monteiro",
            "age": 30,
            "cpf": "55566677788",
            "email": "lucas@example.com",  # duplicado
            "phone": "11999999999",
            "username": "lucas2",
            "password": "strongpass"
        }
        serializer = UserRegisterSerializer(data=data)
        assert serializer.is_valid() is False
        assert "email" in serializer.errors

    def test_duplicate_cpf_raises_error(self):
        CustomUser.objects.create_user(
            username="lucas1",
            password="test123",
            name="Lucas",
            last_name="Monteiro",
            email="lucas1@example.com",
            cpf="12345678901"
        )
        data = {
            "name": "Lucas",
            "last_name": "Monteiro",
            "age": 30,
            "cpf": "12345678901",  # duplicado
            "email": "lucas2@example.com",
            "phone": "11999999999",
            "username": "lucas2",
            "password": "strongpass"
        }
        serializer = UserRegisterSerializer(data=data)
        assert serializer.is_valid() is False
        assert "cpf" in serializer.errors
