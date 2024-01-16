from flask import request
from flask_restx import Resource, Namespace
from project.container import user_service
from project.setup.api.models import user
from project.setup.api.parsers import page_parser
from project.decorators.user import admin_required

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    @user_ns.expect(page_parser)
    @user_ns.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all users   .
        """
        return user_service.get_all(**page_parser.parse_args())

    def post(self):
        user = user_service.create(request.json)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserViews(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        res = UserSchema().dump(user)
        return res, 200

    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
