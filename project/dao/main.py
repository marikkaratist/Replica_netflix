from project.dao.base import BaseDAO
from project.models import Genre


class GenreDAO(BaseDAO[Genre]):
    __model__ = Genre
