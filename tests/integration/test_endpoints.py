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

def test_add_user_bad_group_request(client: FlaskClient) -> None:
    response = client.post("/users", json = {"first_name" : "John", "last_name" : "Doe", "birth_year" : 1980, "group" : "wodiwoiwfi"})
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_get_user(client: FlaskClient) -> None:
    client.post("/users", json={"first_name": "John","last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    response = client.get(f"/users/{0}")
    assert response.status_code == HTTPStatus.OK

def test_get_user_not_found(client: FlaskClient) -> None:
    response = client.get(f"/users/{randint(0, 100)}")
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_patch_user(client: FlaskClient) -> None:
    client.post("/users", json={"first_name": "John","last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    response = client.patch("/users/0", json={"first_name": "Jean","last_name": "Pig", "birth_year": 1999, "group": "User"})
    assert response.status_code == HTTPStatus.OK

def test_patch_user_bad_group_request(client: FlaskClient) -> None:
    client.post("/users", json={"first_name": "John","last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    response = client.patch("/users/0", json={"first_name": "Jean","last_name": "Pig", "birth_year": 1999, "group": "owkdowkdow"})
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_patch_user_does_not_exist(client:FlaskClient) -> None:
    client.post("/users", json={"first_name": "John","last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    response = client.patch("/users/3000", json={"first_name": "Jean","last_name": "Pig", "birth_year": 1999, "group": "User"})
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_delete_user(client:FlaskClient) -> None:
    client.post("/users", json={"first_name": "John","last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    response = client.delete("/users/0")
    assert response.status_code == HTTPStatus.OK

def test_delete_user_does_not_exist(client:FlaskClient)-> None:
    response = client.delete("/users/3000")
    assert response.status_code == HTTPStatus.NOT_FOUND    