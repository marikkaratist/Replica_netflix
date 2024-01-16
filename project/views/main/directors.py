from flask import request
from flask_restx import Resource, Namespace
from project.container import director_service
from project.setup.api.models import director
from project.setup.api.parsers import page_parser
from project.decorators.user import admin_required, auth_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    @director_ns.expect(page_parser)
    @director_ns.marshal_with(director, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all directors.
        """
        return director_service.get_all(**page_parser.parse_args())

    @admin_required
    def post(self):
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201, {"location": f"/users/{director.id}"}


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    @director_ns.response(404, 'Not Found')
    @director_ns.marshal_with(director, code=200, description='OK')
    def get(self, director_id: int):
        """
        Get director by id.
        """
        return genre_service.get_item(director_id)

    @admin_required
    def put(self, rid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = rid
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, rid):
        director_service.delete(rid)
        return "", 204
