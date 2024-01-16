from flask import Flask, render_template, jsonify
from flask_cors import CORS

from project.exceptions import BaseServiceError
from project.setup.api import api
from project.setup.db import db
from project.views.auth import auth_ns, user_ns
from project.views.main import director_ns, genre_ns, movie_ns


def base_service_error_handler(exception: BaseServiceError):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.route('/')
    def index():
        return render_template('index.html', posts=posts)

    db.init_app(app)
    CORS(app=app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)

    app.register_error_handler(BaseServiceError, base_service_error_handler)

    return app
