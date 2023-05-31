import typing as t

from app.db import models as m
from app.schemas import user_subscriptions as s
from fastapi import HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError


def get_list() -> t.List[s.UserSubscriptionGet]:
    user_subs = db.session.query(m.UserSubscription).all()
    schemas = [s.UserSubscriptionGet.from_orm(user_sub) for user_sub in user_subs]
    return schemas


def get(user_sub_id: str) -> s.UserSubscriptionGet:
    user_sub = (
        db.session.query(m.UserSubscription)
        .where(m.UserSubscription.id == user_sub_id)
        .one_or_none()
    )
    return s.UserSubscriptionGet.from_orm(user_sub)


def create(payload: s.UserSubscriptionCreate) -> s.UserSubscriptionGet:
    user_sub = m.UserSubscription(**payload.dict())
    try:
        db.session.add(user_sub)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise HTTPException(
            status_code=500,
            detail="Integrity error occured while trying to add a new record.",
        )

    return s.UserSubscriptionGet.from_orm(user_sub)
