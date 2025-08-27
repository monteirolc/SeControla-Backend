import pytest
from login.serializers import UserLoginSerializer
from login.models import CustomUser


@pytest.mark.django_db
class TestUserLoginSerializer:
    def test_valid_login_credentials(self):
        CustomUser.objects.create_user(
            username="testuser",
            password="testpass123",
            name="Test",
            last_name="User",
            email="test@example.com",
            cpf="12345678901"
        )

        data = {"username": "testuser", "password": "testpass123"}
        serializer = UserLoginSerializer(data=data)

        assert serializer.is_valid() is True
        assert serializer.validated_data["username"] == "testuser"

    def test_invalid_password(self):
        CustomUser.objects.create_user(
            username="testuser",
            password="correctpass",
            name="Test",
            last_name="User",
            email="test@example.com",
            cpf="12345678901"
        )

        data = {"username": "testuser", "password": "wrongpass"}
        serializer = UserLoginSerializer(data=data)

        assert serializer.is_valid() is False
        assert "Invalid login credentials" in str(serializer.errors)

    def test_nonexistent_user(self):
        data = {"username": "ghost", "password": "somepass"}
        serializer = UserLoginSerializer(data=data)

        assert serializer.is_valid() is False
        assert "Invalid login credentials" in str(serializer.errors)

    def test_missing_fields(self):
        data = {"username": "testuser"}  # sem senha
        serializer = UserLoginSerializer(data=data)

        assert serializer.is_valid() is False
        assert "password" in serializer.errors
