from http import HTTPStatus
import json


def test_get_register_route(test_client):
    response = test_client.get('/register')
    assert response.status_code == HTTPStatus.OK


def test_post_register(test_client, common_user_uuid):
    response = test_client.post('/register',
                            json={
                                **common_user_uuid
                            })
    assert response.status_code == HTTPStatus.CREATED


def test_get_login(test_client):
    response = test_client.get('/login')
    assert response.status_code == HTTPStatus.OK


def test_login(test_client, common_user_uuid):
    dataJson = json.dumps({'email': common_user_uuid['email'], 'password': common_user_uuid['password']})
    response = test_client.post(
        '/login',
        data=dataJson
    )
    assert response.status_code == HTTPStatus.OK


