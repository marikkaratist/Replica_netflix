from project.config import DevelopmentConfig
from project.dao.models import *  # noqa F401, F403
from project.server import create_app
from project.setup_db import db

app = create_app(DevelopmentConfig)

with app.app_context():
    db.drop_all()
    db.create_all()
