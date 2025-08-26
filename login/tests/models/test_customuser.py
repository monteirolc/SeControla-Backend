# tests/test_models.py
import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()


@pytest.mark.django_db
def test_create_user_ok():
    user = User.objects.create_user(
        username="john_doe",
        email="john@example.com",
        password="secret123",
        name="John",
        last_name="Doe",
        cpf="12345678901",
        age=25,
        phone="11999999999"
    )
    assert user.pk is not None
    assert user.username == "john_doe"
    assert str(user) == "john_doe"
    assert user.email == "john@example.com"
    assert user.age == 25
    assert user.check_password("secret123")  # senha foi setada corretamente


@pytest.mark.django_db
def test_create_superuser_flags():
    su = User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="supersecret",
        name="Admin",
        last_name="Master",
        cpf="98765432100",
    )
    assert su.is_staff is True
    assert su.is_superuser is True
    assert str(su) == "admin"


@pytest.mark.django_db
def test_username_unico():
    User.objects.create_user(
        username="unique",
        email="unique@example.com",
        password="123",
        name="User",
        last_name="One",
        cpf="11122233344",
    )
    with pytest.raises(IntegrityError):
        User.objects.create_user(
            username="unique",
            email="another@example.com",
            password="123",
            name="User",
            last_name="Two",
            cpf="55566677788",
        )


@pytest.mark.django_db
def test_email_unico():
    User.objects.create_user(
        username="user1",
        email="same@example.com",
        password="123",
        name="User",
        last_name="One",
        cpf="12312312312",
    )
    with pytest.raises(IntegrityError):
        User.objects.create_user(
            username="user2",
            email="same@example.com",
            password="123",
            name="User",
            last_name="Two",
            cpf="32132132132",
        )


@pytest.mark.django_db
def test_cpf_unico():
    User.objects.create_user(
        username="cpfuser1",
        email="cpf1@example.com",
        password="123",
        name="User",
        last_name="One",
        cpf="00011122233",
    )
    with pytest.raises(IntegrityError):
        User.objects.create_user(
            username="cpfuser2",
            email="cpf2@example.com",
            password="123",
            name="User",
            last_name="Two",
            cpf="00011122233",  # mesmo cpf
        )


@pytest.mark.django_db
def test_age_opcional():
    """Deve ser possível criar usuário sem informar idade."""
    user = User.objects.create_user(
        username="noage",
        email="noage@example.com",
        password="123",
        name="User",
        last_name="NoAge",
        cpf="44455566677",
    )
    assert user.age is None
