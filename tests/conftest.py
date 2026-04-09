import pytest
from app import create_app, db
from app.models import User
from config import TestConfig
from tests.utils.auth import AuthAction

@pytest.fixture
def app():
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth(client):
    return AuthAction(client)
