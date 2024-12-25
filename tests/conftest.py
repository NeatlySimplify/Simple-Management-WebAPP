from http import HTTPStatus
import json
from pickletools import pyset
import random
from faker import Faker
from fastapi.testclient import TestClient
import playwright
from app.Model.clients import ClientsType, RelationshipTag, SexTag
from app.main import app
import pytest
from playwright.async_api import async_playwright, BrowserContext



fake = Faker("pt_BR")


@pytest.fixture
def test_client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
def admin_uuid():
    admin = {
        "name": fake.name_male(),
        "email": fake.free_email(),
        "password": fake.password(10, False, True, True)
    }
    return admin


@pytest.fixture(scope="session")
def common_user_uuid():
    user = {
        "name": fake.name_male(),
        "email": fake.free_email(),
        "password": fake.password(10, False, True, True)
    }
    return user


@pytest.fixture
def random_user():
    user = {
        "name": fake.name_male(),
        "email": fake.free_email(),
        "password": fake.password(10, False, True, True)
    }
    return user


@pytest.fixture
def random_client():
    client = {
        'email': fake.free_email(),
        'name': fake.name(),
        'sex': random.choice(list(SexTag)),
        'relationship': random.choice(list(RelationshipTag)),
        'govt_id': fake.isbn13(),
        'type_client': random.choice(list(ClientsType)),
        'birth': fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat() + "T00:00:00",
        'template_model': '',
        'details': '',
        'custom_fields': []
    }
    return client

@pytest.fixture
def test_logged(test_client, common_user_uuid):
    response_register = test_client.post('/register',
                            json={
                                **common_user_uuid
                            })
    print(response_register.json())
    assert response_register.status_code == HTTPStatus.CREATED

    dataJson = json.dumps({'email': common_user_uuid['email'], 'password': common_user_uuid['password']})
    response_login = test_client.post(
        '/login',
        data=dataJson
    )
    assert response_login.status_code == HTTPStatus.OK
    token = response_login.cookies.get('access_token')
    test_client.cookies.set(name='access_token', value=token)
    return test_client

@pytest.fixture
def address():
    pass


@pytest.fixture
def phone_number():
    pass

@pytest.fixture(scope='function')
def browser_context():
    playwright = async_playwright.start()
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    yield context
    context.close()
    browser.close()
