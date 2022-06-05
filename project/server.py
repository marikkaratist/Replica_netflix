from flask import Flask
from flask_cors import CORS

from project.setup.api import api
from project.setup.db import db
from project.views import auth_ns, genres_ns, user_ns


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    CORS(app=app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(genres_ns)

    return app
