from project.dao import GenresDAO

from project.services import GenresService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
