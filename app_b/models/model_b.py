from sqlalchemy import Column, String

from .base import Base


class ModelB(Base):
    __tablename__ = "table_b"

    property_b = Column(String(100), nullable=False)
