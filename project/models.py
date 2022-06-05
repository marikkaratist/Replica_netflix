from project.setup.db import db, models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = db.Column(db.String(100), unique=True, nullable=False)
    # TODO: [models] После добавления моделей на фильмы и пользователей, раскомментировать эти поля
    # movies = db.relationship('Movie', back_populates='genre', cascade='delete')
    # users = db.relationship('User', back_populates='genre')
