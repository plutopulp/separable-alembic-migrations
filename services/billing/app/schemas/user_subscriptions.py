from datetime import datetime

from common.schemas.base import BaseModel


class UserSubscriptionBase(BaseModel):
    user_id: str
    subscription_id: str


class UserSubscriptionCreate(UserSubscriptionBase):
    pass


class UserSubscriptionGet(UserSubscriptionBase):
    id: str
    created_at: datetime
    updated_at: datetime
