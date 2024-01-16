from project.models import User
from project.dao.main import UsersDAO
from project.tools.security import generate_password_hash
from project.setup.db import db


class UsersService:
    def __init__(self, dao: UsersDAO):
        self.session = db.session
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_username(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user_d: dict) -> dict:
        user_d['password'] = self.generate_password_hash(user_d['password'])
        return self.dao.create(user_d)

    def update(self, user_d):
        user_d['password'] = self.generate_password_hash(user_d['password'])
        return self.dao.update(user_d)

    def delete(self, uid):
        self.dao.delete(uid)
