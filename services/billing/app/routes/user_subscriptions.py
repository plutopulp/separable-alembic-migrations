import typing as t

from app.schemas import user_subscriptions as s
from app.services import user_subscriptions as service
from fastapi.routing import APIRouter

router = APIRouter(prefix="/user-subscriptions", tags=["user-subscriptions"])


@router.get("/{user_sub_id}", response_model=s.UserSubscriptionGet)
def read(user_sub_id: str):
    return service.get(user_sub_id)


@router.post("", response_model=s.UserSubscriptionGet)
def create(payload: s.UserSubscriptionCreate):
    user_sub = service.create(payload)
    return user_sub


@router.get("", response_model=t.List[s.UserSubscriptionGet])
def index():
    return service.get_list()
