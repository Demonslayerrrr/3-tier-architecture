from http import HTTPStatus
from random import randint
from flask.testing import FlaskClient
from src.app import app
from pytest import fixture

@fixture
def client() -> FlaskClient:
    return app.test_client()

def test_get_users(client: FlaskClient) -> None:
    response = client.get("/users")
    assert response.status_code == HTTPStatus.OK

def test_add_user(client: FlaskClient) -> None:
    response = client.post("/users", json={"first_name": "John","last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    assert response.status_code == HTTPStatus.CREATED

def test_get_user(client: FlaskClient) -> None:
    client.post("/users", json={"first_name": "John","last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    response = client.get(f"/users/{0}")
    assert response.status_code == HTTPStatus.OK

def test_get_user_not_found(client: FlaskClient) -> None:
    response = client.get(f"/users/{randint(0, 100)}")
    assert response.status_code == HTTPStatus.NOT_FOUND

