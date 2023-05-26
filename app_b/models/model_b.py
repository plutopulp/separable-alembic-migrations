from sqlalchemy import Column, String

from .base import Base


class ModelB(Base):
    __tablename__ = "table_b"

    property_b = Column(String(100), nullable=False)
    other = Column(String(100), nullable=False)
    other_2 = Column(String(100), nullable=False)
