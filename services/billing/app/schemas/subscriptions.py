from datetime import datetime

from common.schemas.base import BaseModel


class SubscriptionBase(BaseModel):
    category: str
    price: int


class SubscriptionCreate(SubscriptionBase):
    pass


class SubscriptionGet(SubscriptionBase):
    id: str
    created_at: datetime
    updated_at: datetime
