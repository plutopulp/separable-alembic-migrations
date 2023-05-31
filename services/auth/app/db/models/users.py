from sqlalchemy import Column, String

from .base import Base


class User(Base):
    __tablename__ = "user"

    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
