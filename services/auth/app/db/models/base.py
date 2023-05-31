import os
import random
import string
import uuid

from sqlalchemy import Column, DateTime, MetaData, String, func
from sqlalchemy.orm import registry


def generate_id(table_name: str, length: int = 15) -> str:
    id = (
        table_name
        + "_"
        + "".join(
            random.SystemRandom().choice(string.ascii_lowercase + string.digits)
            for _ in range(length)
        )
    )
    return id


mapper_registry = registry()
_Base = mapper_registry.generate_base()


class Base(_Base):
    """Base class for all API models."""

    __abstract__ = True

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.current_timestamp(),
        nullable=False,
    )

    metadata = MetaData(schema=os.environ["DB_SCHEMA_AUTH"])

    @classmethod
    def _generate_model_id(cls):
        return f"{cls.__tablename__}_{uuid.uuid4().hex}"

    id = Column(
        String(),
        # Define a default in case a derived class did not call our __init__
        default=_generate_model_id,
        primary_key=True,
    )

    def __init__(self, **kwargs):
        self.id = kwargs.pop("id", self._generate_model_id())
        super().__init__(**kwargs)
