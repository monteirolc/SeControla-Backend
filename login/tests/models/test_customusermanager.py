import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestCustomUserManager:

    def test_create_user_success(self):
        user = User.objects.create_user(
            username="lucas",
            password="test123",
            name="Lucas",
            last_name="Monteiro",
            email="lucas@example.com",
            cpf="12345678901"
        )
        assert user.username == "lucas"
        assert user.check_password("test123")
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser

    def test_create_user_without_username_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            User.objects.create_user(
                username=None,
                password="test123",
                name="Lucas",
                last_name="Monteiro",
                email="lucas@example.com",
                cpf="12345678901"
            )
        assert "The given username must be set" in str(excinfo.value)

    def test_create_superuser_success(self):
        admin = User.objects.create_superuser(
            username="admin",
            password="admin123",
            name="Admin",
            last_name="Root",
            email="admin@example.com",
            cpf="98765432100"
        )
        assert admin.username == "admin"
        assert admin.check_password("admin123")
        assert admin.is_staff
        assert admin.is_superuser

    def test_create_superuser_without_is_staff_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            User.objects.create_superuser(
                username="admin2",
                password="admin123",
                name="Admin",
                last_name="Root",
                email="admin2@example.com",
                cpf="11122233344",
                is_staff=False
            )
        assert "Superuser must have is_staff=True" in str(excinfo.value)

    def test_create_superuser_without_is_superuser_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            User.objects.create_superuser(
                username="admin3",
                password="admin123",
                name="Admin",
                last_name="Root",
                email="admin3@example.com",
                cpf="22233344455",
                is_superuser=False
            )
        assert "Superuser must have is_superuser=True" in str(excinfo.value)
