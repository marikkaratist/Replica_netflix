from project.dao.main import GenresDAO, DirectorsDAO, MoviesDAO, UsersDAO

from project.services.auth.auths_service import AuthsService
from project.services.main.directors_service import DirectorsService
from project.services.main.genres_service import GenresService
from project.services.main.movies_service import MoviesService
from project.services.auth.users_service import UsersService
from project.setup.db import db

# DAO
director_dao = DirectorsDAO(db.session)
genre_dao = GenresDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UsersDAO(db.session)
# Services
director_service = DirectorsService(dao=director_dao)
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(dao=user_dao)
auth_service = AuthsService(user_service)
