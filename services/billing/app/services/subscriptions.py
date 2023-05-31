import typing as t

from app.db import models as m
from app.schemas import subscriptions as s
from fastapi import HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError


def get_list() -> t.List[s.SubscriptionGet]:
    subscriptions = db.session.query(m.Subscription).all()
    schemas = [
        s.SubscriptionGet.from_orm(subscription) for subscription in subscriptions
    ]
    return schemas


def get(subscription_id: int) -> s.SubscriptionGet:
    subscription = (
        db.session.query(m.Subscription)
        .where(m.Subscription.id == subscription_id)
        .one_or_none()
    )
    return s.SubscriptionGet.from_orm(subscription)


def create(payload: s.SubscriptionCreate) -> s.SubscriptionGet:
    subscription = m.Subscription(**payload.dict())
    try:
        db.session.add(subscription)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise HTTPException(
            status_code=500,
            detail="Integrity error occured while trying to add a new record.",
        )

    return s.SubscriptionGet.from_orm(subscription)
