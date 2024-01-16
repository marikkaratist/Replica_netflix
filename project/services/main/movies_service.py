from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Movie]:
        if page.get("director_id") is not None:
            movies = self.dao.get_by_director_id(page.get("director_id"))
        elif page.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(page.get("genre_id"))
        elif page.get("year") is not None:
            movies = self.dao.get_by_year(page.get("year"))
        else:
            movies = self.dao.get_all(page=page)
        return movies

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)

