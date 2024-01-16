import jwt
from flask import abort, request
from project.config import BaseConfig

base_config = BaseConfig()


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        try:
            user = jwt.decode(token, base_config.SECRET_KEY, algorithms=[base_config.JWT_ALGO])
            role = user.get("role")
            if role != "admin":
                abort(403)

        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        try:
            jwt.decode(token, base_config.SECRET_KEY, algorithms=[base_config.JWT_ALGO])

        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper
