from project.dao.base import BaseDAO
from project.models import Genre


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre
