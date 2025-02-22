from src.app import app
from flask import Flask

def test_app_is_flask_instance():
    assert isinstance(app, Flask)

