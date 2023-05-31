from datetime import datetime

from .base import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    pass


class UserGet(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime
