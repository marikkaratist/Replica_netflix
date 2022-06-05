import pytest

from project.config import TestingConfig
from project.models import Genre
from project.server import create_app
from project.setup.db import db as database


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        yield app


@pytest.fixture
def db(app):
    database.init_app(app)
    database.drop_all()
    database.create_all()
    database.session.commit()

    yield database

    database.session.rollback()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client


@pytest.fixture
def genre(db):
    obj = Genre(name="genre")
    db.session.add(obj)
    db.session.commit()
    return obj
