from sqlalchemy import Column, String

from .base import Base


class ModelA(Base):
    __tablename__ = "table_a"

    property_a = Column(String(100), nullable=False)
    other_property = Column(String(100), nullable=False)
