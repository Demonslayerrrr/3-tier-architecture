from flask import Flask
from src.controller import UserController 
from pytest import fixture
from unittest.mock import Mock
from src.repository import UserRepository

@fixture
def repository() -> Mock:
    return Mock(UserRepository)

@fixture
def controller(repository: Mock) -> UserController:
    return UserController(repository=repository)

def test_controller_get_users(controller:UserController,repository:Mock) -> None:
    repository.get_users.return_value = {"0": {"first_name": "John", "last_name": "Doe", "age": 41, "group": "Admin"}}
    actual_return, status_code = controller.get_users()
    expected_return = {"0": {"first_name": "John", "last_name": "Doe", "age": 41, "group": "Admin"}}
    assert actual_return == expected_return

def test_controller_get_user(controller:UserController,repository:Mock) -> None:
    repository.get_user.return_value = {"first_name": "John", "last_name": "Doe", "age": 41, "group": "Admin"}
    actual_return, _ = controller.get_user(0)
    expected_return = {"first_name": "John", "last_name": "Doe", "age": 41, "group": "Admin"}
    assert actual_return == expected_return

def test_controller_get_user_with_invalid_id(controller:UserController,repository:Mock) -> None:
    repository.get_user.side_effect = KeyError()
    actual_return, _ = controller.get_user(0)
    expected_return = {"message":"User not found"}
    assert actual_return == expected_return


def test_controller_add_user(controller:UserController,repository:Mock) -> None:
    controller.add_user({"first_name": "John", "last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    repository.add_user.assert_called_once_with({"first_name": "John", "last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    assert repository.add_user.called

def test_controller_add_user_with_invalid_group(controller:UserController,repository:Mock) -> None:
    repository.add_user.side_effect = ValueError()
    actual_return, _ = controller.add_user({"first_name": "John", "last_name": "Doe", "birth_year": 1980, "group": "wodiwoiwfi"})
    expected_return = {"message":"Group does not exist"}
    assert actual_return == expected_return

def test_controller_patch_user(controller:UserController,repository:Mock) -> None:
    controller.patch_user(0, {"first_name": "Jean","last_name": "Pig", "birth_year": 1999, "group": "User"})
    repository.patch_user.assert_called_once_with(0, {"first_name": "Jean","last_name": "Pig", "birth_year": 1999, "group": "User"})
    assert repository.patch_user.called

def test_controller_patch_user_with_invalid_group(controller:UserController,repository:Mock) -> None:
    repository.patch_user.side_effect = ValueError()
    actual_return, _ = controller.patch_user(0, {"first_name": "Jean","last_name": "Pig", "birth_year": 1999, "group": "owkdowkdow"})
    expected_return = {"message":"Group does not exist"}
    assert actual_return == expected_return

def test_controller_patch_user_with_invalid_id(controller:UserController,repository:Mock) -> None:
    repository.patch_user.side_effect = KeyError()
    actual_return, _ = controller.patch_user(0, {"first_name": "Jean","last_name": "Pig", "birth_year": 1999, "group": "User"})
    expected_return = {"message":"User not found"}
    assert actual_return == expected_return

def test_controller_delete_user(controller:UserController,repository:Mock) -> None:
    controller.delete_user(0)
    repository.delete_user.assert_called_once_with(0)
    assert repository.delete_user.called

def test_controller_delete_user_with_invalid_id(controller:UserController,repository:Mock) -> None:
    repository.delete_user.side_effect = KeyError()
    actual_return, _ = controller.delete_user(0)
    expected_return = {"message":"User not found"}
    assert actual_return == expected_return