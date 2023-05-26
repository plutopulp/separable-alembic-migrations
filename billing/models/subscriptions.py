from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Subscription(Base):
    __tablename__ = "subscription"

    category = Column(String(64), nullable=False)
    price = Column(Integer, nullable=False)


class UserSubscription(Base):
    __tablename__ = "user_subscription"
    user_id = Column(String(128), nullable=False)
    subscription_id = Column(
        ForeignKey("subscription.id", ondelete="SET NULL"), index=True
    )

    subscription = relationship("Subscription", back_populates="user_subscriptions")
