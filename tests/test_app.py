from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app

import pytest


@pytest.fixture()
def client():
    return TestClient(app)


def test_read_root(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def test_create_client(client):
    response = client.post(
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
