import pytest

from project.config import TestingConfig
from project.dao import GenreDAO
from project.server import create_app
from project.services import GenresService
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

    database.session.close()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client


@pytest.fixture
def genres_dao(db):
    return GenreDAO(db.session)


@pytest.fixture
def genres_service(genres_dao):
    return GenresService(genres_dao)
