# ** App Modules
from app.service.base import BaseService
from app.models.user import User
from app.helper.decorator import db
# ** External Modules
from logzero import logger


class UserService(BaseService):
    def __init__(self, symbol=None):
        super().__init__(User)

    @db('activate_user')
    def activate(self, user: User):
        user.activate()
        logger.info(f'User is Active | {user.email}')

    @db('deactivate_user')
    def deactivate(self, user: User):
        user.deactivate()
        logger.info(f'User is In-Active | {user.email}')

    @db('insert_stock')
    def insert(self, user: User):
        data = User(
            name='bala',
            email='bala@example.com',
            is_active=True
        )
        self.s.add(data)
        logger.info(f'New User Added | {data.email}')
