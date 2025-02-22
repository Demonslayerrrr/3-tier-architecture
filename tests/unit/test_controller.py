from flask import Flask
from src.controller import UserController as controller
from pytest import raises

def test_controller_can_be_instantiated():
    with raises(NotImplementedError):
        controller()