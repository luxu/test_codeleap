import pytest

from rest_framework.test import APIClient

from faker import Faker

from core.models import Careers

from django.contrib.auth.models import User

fake = Faker('pt_BR')  # Using Brazilian Portuguese locale

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def career(db):
    data = {
        "title": "Example Post Title",
        "content": "This is the content of my post.",
        'username': fake.name(),
        'author_ip': '127.0.0.1',
    }
    return Careers.objects.create(**data)

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def token(client, user):
    return client.post(
        '/api/token-auth/',
        {
            'username': 'testuser',
            'password': 'testpassword'
        }
    ).data['token']