from datetime import date, datetime
from http import HTTPStatus


import pytest
from fastapi.testclient import TestClient

from app.main import app

from app.Routes import user








class Phone:
    type: list = [
        choice("Residencial", "Trabalho", "Outro"),
        choice("Celular", "Telefone Fixo")
    ]
    numero = fake.phone_number()
    contato: str = choice()


# End Dataclasses


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root(fake):
    response = fake.get('/')
    assert response.status_code == HTTPStatus.OK


def test_create_fake(fake):
    response = fake.post(
        '/',
        json={
            'nome': 'teste',
            'senha': '12456',
            'email': 'ribeirodennis9@gmail.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'nome': 'teste',
        'email': 'ribeirodennis9@gmail.com',
    }
