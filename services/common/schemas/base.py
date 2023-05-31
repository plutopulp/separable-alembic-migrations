from datetime import datetime

from pydantic import BaseModel as PydanticModel


class BaseConfig:
    allow_population_by_field_name = True
    json_encoders = {datetime: datetime.timestamp}
    orm_mode = True


class BaseModel(PydanticModel):
    class Config(BaseConfig):
        pass
