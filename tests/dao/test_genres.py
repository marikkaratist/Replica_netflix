import pytest

from project.models import Genre


class TestGenreDAO:

    @pytest.fixture
    def genre_1(self, db):
        g = Genre(name="Боевик")
        db.session.add(g)
        db.session.commit()
        return g

    @pytest.fixture
    def genre_2(self, db):
        g = Genre(name="Комедия")
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_genre_by_id(self, genre_1, genres_dao):
        assert genres_dao.get_by_id(genre_1.id) == genre_1

    def test_get_genre_by_id_not_found(self, genres_dao):
        assert not genres_dao.get_by_id(1)

    def test_get_all_genres(self, genres_dao, genre_1, genre_2):
        assert genres_dao.get_all() == [genre_1, genre_2]
