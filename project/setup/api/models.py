from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Баз Лурман'),
})
movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Донни Дарко'),
    'description': fields.String(required=True, max_length=100, example='К своим 16 годам старшеклассник Донни уже знает, что такое смерть.'),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=9H_t5cdszFU'),
    'year': fields.Integer(required=True, max_length=100, example='2001'),
    'rating': fields.Integer(required=True, max_length=100, example='8'),
})
user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='nero@mail.ru'),
    'password': fields.String(required=True, max_length=100, example='sd545f45f4g4gf'),
    'role': fields.String(required=True, max_length=100, example='user'),
})
