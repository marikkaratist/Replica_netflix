from flask import request
from flask_restx import Namespace, Resource
from project.container import genre_service
from project.setup.api.models import genre
from project.setup.api.parsers import page_parser
from project.decorators.user import admin_required, auth_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    @genre_ns.expect(page_parser)
    @genre_ns.marshal_with(genre, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all genres.
        """
        return genre_service.get_all(**page_parser.parse_args())

    @admin_required
    def post(self):
        req_json = request.json
        genre = genre_service.create(req_json)
        return "", 201, {"location": f"/users/{genre.id}"}


@genre_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    @auth_required
    # @genre_ns.response(404, 'Not Found')
    @genre_ns.marshal_with(genre, code=200, description='OK')
    def get(self, genre_id: int):
        """
        Get genre by id.
        """
        return genre_service.get_item(genre_id)

    @admin_required
    def put(self, rid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = rid
        genre_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, rid):
        genre_service.delete(rid)
        return "", 204

