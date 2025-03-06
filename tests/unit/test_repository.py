from src.repository import UserRepository 
from pytest import fixture, raises
from datetime import date

@fixture
def repository():
    return UserRepository()

def test_get_users(repository:UserRepository) -> None:
    repository.add_user({"first_name": "John", "last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    actual = repository.get_users()
    assert actual == {0: {"first_name": "John", "last_name": "Doe", "age": date.today().year - 1980, "group": "Admin"}}

def test_get_user(repository:UserRepository) -> None:
    repository.add_user({"first_name": "John", "last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    actual = repository.get_user(0)
    assert actual ==  {"first_name": "John", "last_name": "Doe", "age": date.today().year-1980, "group": "Admin"}

def test_get_user_invalid_id(repository:UserRepository) -> None:
    with raises(KeyError):
        repository.get_user(3000)

def test_add_user(repository:UserRepository) -> None:
    repository.add_user({"first_name": "John", "last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    assert repository.users != {}

def test_add_user_invalid_group(repository:UserRepository) -> None:
    with raises(ValueError):   
        repository.add_user({"first_name": "John", "last_name": "Doe", "birth_year": 1980, "group": "fjeifjeoijfjoihef"})

def test_patch_user(repository:UserRepository) -> None:
    repository.add_user({"first_name": "John", "last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    repository.patch_user(0,{"first_name": "Jack", "last_name": "Duck", "birth_year": 1985, "group": "Premium"})
    actual = repository.get_user(0)
    assert actual == {"first_name": "Jack", "last_name": "Duck", "age": date.today().year-1985, "group": "Premium"}

def test_patch_user_invalid_id(repository:UserRepository) -> None:
    repository.add_user({"first_name": "John", "last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    with raises(KeyError):
        repository.patch_user(3000,{"first_name": "Jack", "last_name": "Duck", "birth_year": 1985, "group": "Premium"})

def test_patch_user_invalid_group(repository:UserRepository) -> None:
    repository.add_user({"first_name": "John", "last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    with raises(ValueError):
        repository.patch_user(0,{"first_name": "Jack", "last_name": "Duck", "birth_year": 1985, "group": "fiwifhfihew"})

def test_delete_user(repository:UserRepository) -> None:
    repository.add_user({"first_name": "John", "last_name": "Doe", "birth_year": 1980, "group": "Admin"})
    repository.delete_user(0)
    assert repository.users == {}