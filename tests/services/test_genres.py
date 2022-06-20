import pytest

from project.exceptions import ItemNotFound
from project.models import Genre


class TestGenresService:

    @pytest.fixture
    def genre(self, db):
        obj = Genre(name="genre")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_genre(self, genres_service, genre):
        assert genres_service.get_item(genre.id)

    def test_genre_not_found(self, genres_service):
        with pytest.raises(ItemNotFound):
            genres_service.get_item(10)
