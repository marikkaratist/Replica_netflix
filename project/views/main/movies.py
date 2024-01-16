from flask import request
from flask_restx import Resource, Namespace
from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser
from project.decorators.user import admin_required, auth_required

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    @movie_ns.expect(page_parser)
    @movie_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """
        return movie_service.get_all(**page_parser.parse_args())

    @admin_required
    def post(self):
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required
    @movie_ns.response(404, 'Not Found')
    @movie_ns.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        return genre_service.get_item(movie_id)

    @admin_required
    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, bid):
        movie_service.delete(bid)
        return "", 204
