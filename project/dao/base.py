from typing import Generic, List, Optional, TypeVar

from flask import current_app
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import scoped_session
from werkzeug.exceptions import NotFound
from project.setup.db.models import Base

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    __model__ = Base

    def __init__(self, db_session: scoped_session) -> None:
        self._db_session = db_session

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

    def get_by_id(self, pk: int) -> Optional[T]:
        return self._db_session.query(self.__model__).get(pk)

    def get_all(self, page: Optional[int] = None) -> List[T]:
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

    def get_by_director_id(self, val):
        return self._db_session.query(self.__model__.director_id == val).all()

    def get_by_genre_id(self, val):
        return self._db_session.query(self.__model__.genre_id == val).all()

    def get_by_year(self, val):
        return self._db_session.query(self.__model__.year == val).all()

    def create(self, stmt_d):
        stmt = Genre(**stmt_d)
        self.session.add(stmt)
        self.session.commit()
        return ent

    def delete(self, pk: int) -> Optional[T]:
        stmt = self.get_by_id(pk)
        self.session.delete(stmt)
        self.session.commit()

    def update(self, stmt_d):
        stmt = self.get_one(stmt_d.get("id"))
        stmt.name = stmt_d.get("name")
        stmt.title = stmt_d.get("title")
        stmt.description = stmt_d.get("description")
        stmt.trailer = stmt_d.get("trailer")
        stmt.year = stmt_d.get("year")
        stmt.rating = stmt_d.get("rating")
        stmt.genre_id = stmt_d.get("genre_id")
        stmt.director_id = stmt_d.get("director_id")
        stmt.email = stmt_d.get("email")
        stmt.password = stmt_d.get("password")

        self.session.add(stmt)
        self.session.commit()
