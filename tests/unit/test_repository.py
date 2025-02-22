from src.repository import UserRepository as repository
from pytest import raises

def test_repository_can_be_instantiated():
    with raises(NotImplementedError):
        repository()