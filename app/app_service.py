# ** App Modules
from app.helper.logger import setup_log
from app.db import get_db


def register_logger():
    setup_log()


def db():
    return next(get_db())
