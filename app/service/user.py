from app.models.user import User
from app.service.base import BaseService
from app.helper.decorator import db
from app.pyd_models import UserBase


class UserService(BaseService):
    def __init__(self):
        # TODO: Make UserService to Singleton design pattern.
        super().__init__(User)

    def fetch_by_email(self, email: str, active_status=True) -> User:
        res = self.q.filter(User.email == email)

        if active_status:
            res = res.filter(User.is_active)

        return res.first()

    @db('user_deactivate')
    def deactivate(self, email):
        user = self.q.filter(User.email == email).first()
        user.deactivate()

    @db('user_activate')
    def activate(self, email):
        user = self.q.filter(User.email == email).first()
        user.activate()

    def get_user(self, email: str) -> User:
        res: UserBase = self.q.filter(User.email == email).first()
        return res if res else None
