# ** App Modules
from app.db import Base
# ** External Modules
from sqlalchemy import Boolean, Column, Integer, String, DateTime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
