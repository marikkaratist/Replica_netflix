from project.dao import GenreDAO

from project.services import GenresService
from project.setup.db import db

# DAO
genre_dao = GenreDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
