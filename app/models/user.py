from sqlalchemy import Boolean, Column, Integer, String, DateTime
from app.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String, index=True)
    lname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"{self.fname} {self.lname} | {self.id}"

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True
