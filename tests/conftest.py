import random
from faker import Faker
from fastapi.testclient import TestClient
from app.Model.clients import RelationshipTag, SexTag
from app.main import app
import pytest


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
    return {
        'email': fake.free_email(),
        'name': fake.name(),
        'sex': random.choice(list(SexTag).value),
        'relationship': random.choice(list(RelationshipTag).value),
        'birth': fake.date_of_birth(),
        'city': fake.city_name(),
        'state': fake.state_name()
    }

@pytest.fixture
def address():
    pass


@pytest.fixture
def phone_number():
    pass
