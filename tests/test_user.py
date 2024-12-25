from http import HTTPStatus
from playwright.sync_api import expect, Page


def test_get_register_route(test_client):
    response = test_client.get('/register')
    assert response.status_code == HTTPStatus.OK


def test_post_register(test_client, common_user_uuid):
    response = test_client.post(
        '/register',
        json={
            **common_user_uuid
        }
    )
    assert response.status_code == HTTPStatus.CREATED


def test_get_login(test_client):
    response = test_client.get('/login')
    assert response.status_code == HTTPStatus.OK


def test_login(test_client, common_user_uuid):
    response = test_client.post(
        '/login',
        json={
            **common_user_uuid
        }
    )
    assert response.status_code == HTTPStatus.OK

def test_create_client(test_logged, random_client):
    response = test_logged.post(
        '/client/form',
        json={**random_client}
    )
    print(response.json())
    assert response.status_code == 201



