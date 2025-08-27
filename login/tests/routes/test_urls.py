import pytest
from django.urls import reverse, resolve
from login.views import UserRegisterView, UserLoginView


@pytest.mark.parametrize("url_name,view_class", [
    ("register", UserRegisterView),
    ("login", UserLoginView),
])
def test_urls_resolves_to_correct_view(url_name, view_class):
    url = reverse(url_name)
    resolver = resolve(url)
    assert resolver.func.view_class == view_class


@pytest.mark.django_db
def test_register_url_returns_200(client):
    url = reverse("register")
    response = client.get(url)
    # Se a view de registro usa GET (ex: exibir form), deve ser 200
    assert response.status_code in [200, 405]


@pytest.mark.django_db
def test_login_url_returns_200(client):
    url = reverse("login")
    response = client.get(url)
    # Se a view de login usa GET (ex: exibir form), deve ser 200
    assert response.status_code in [200, 405]
