from http import HTTPStatus
from random import randint
from flask.testing import FlaskClient
from src.app import app
from pytest import fixture

@fixture
def client() -> FlaskClient:
    return app.test_client()

def test_get_users(client: FlaskClient):
    response = client.get("/users")
    assert response.status_code == HTTPStatus.OK