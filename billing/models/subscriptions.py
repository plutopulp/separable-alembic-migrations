from sqlalchemy import Column, String, Integer

from .base import Base


class Subscription(Base):
    __tablename__ = "subscription"

    category = Column(String(64), nullable=False)
    price = Column(Integer, nullable=False)
