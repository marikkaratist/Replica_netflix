from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Genre


class GenresService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genre:
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Genre]:
        return self.dao.get_all(page=page)

    def create(self, genre_d):
        return self.dao.create(genre_d)

    def update(self, genre_d):
        self.dao.update(genre_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
