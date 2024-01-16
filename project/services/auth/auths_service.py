import calendar
import datetime
import jwt
from flask import abort
from project.config import BaseConfig
from project.services.auth.users_service import UsersService

base_config = BaseConfig()


class AuthsService:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_by_username(username)
        if user is None:
            raise abort(404)

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, base_config.SECRET_KEY, algorithm=base_config.JWT_ALGO)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, base_config.SECRET_KEY, algorithm=base_config.JWT_ALGO)

        tokens = {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

        return tokens

    def approve_refresh_token(self, refresh_token, data=None):
        data["username"] = jwt.decode(jwt=refresh_token, key=base_config.SECRET_KEY, algorithms=[base_config.JWT_ALGO])

        username = data.get("username")

        return self.generate_tokens(username, None, is_refresh=True)
