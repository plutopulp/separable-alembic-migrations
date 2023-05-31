from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from auth.db.models.users import User


class Subscription(Base):
    __tablename__ = "subscription"

    category = Column(String(64), nullable=False)
    price = Column(Integer, nullable=False)


class UserSubscription(Base):
    __tablename__ = "user_subscription"
    user_id = Column(
        "user_id", ForeignKey(User.id, ondelete="CASCADE"), nullable=False, index=True
    )
    subscription_id = Column(
        ForeignKey("subscription.id", ondelete="SET NULL"), index=True
    )

    subscription = relationship("Subscription", back_populates="user_subscriptions")
