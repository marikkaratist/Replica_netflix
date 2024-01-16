from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from project.setup.db import models, db


class Genre(models.Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)
    genre = relationship("Genre", backref='movies')
    director_id = Column(Integer, ForeignKey("directors.id"), nullable=False)
    director = relationship("Director", backref='movies')


class User(models.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String)