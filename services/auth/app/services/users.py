import typing as t

from app.db import models as m
from app.schemas import users as s
from fastapi import HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError


def get_list() -> t.List[s.UserGet]:
    users = db.session.query(m.User).all()
    schemas = [s.UserGet.from_orm(user) for user in users]
    return schemas


def get(user_id: int) -> s.UserGet:
    user = db.session.query(m.User).where(m.User.id == user_id).one_or_none()
    return s.UserGet.from_orm(user)


def create(payload: s.UserCreate) -> s.UserCreate:
    user = m.User(**payload.dict())
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise HTTPException(
            status_code=500,
            detail="Integrity error occured while trying to add a new record.",
        )

    return s.UserGet.from_orm(user)
