import base64
import os
from pathlib import Path
from typing import Type

BASE_DIR = Path(__file__).resolve().parent.parent


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    JSON_AS_ASCII = False

    ITEMS_PER_PAGE = 12

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130

    PWD_HASH_SALT = base64.b64decode("salt")
    PWD_HASH_ITERATIONS = 100_000

    JWT_ALGO = 'HS256'
    HASH_NAME = 'sha256'

    RESTX_JSON = {
        'ensure_ascii': False,
    }


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR.joinpath('project.db').as_posix()


class ProductionConfig(BaseConfig):
    DEBUG = False
    # TODO: дополнить конфиг
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.getcwd(), "movies.db")}'


class ConfigFactory:
    flask_env = os.getenv('FLASK_ENV', 'production')

    @classmethod
    def get_config(cls) -> Type[BaseConfig]:
        if cls.flask_env == 'development':
            return DevelopmentConfig
        elif cls.flask_env == 'production':
            return ProductionConfig
        elif cls.flask_env == 'testing':
            return TestingConfig
        raise NotImplementedError


config = ConfigFactory.get_config()
