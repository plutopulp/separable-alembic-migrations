import typing as t

from app.schemas import subscriptions as s
from app.services import subscriptions as service
from fastapi.routing import APIRouter

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])


@router.get("/{subscription_id}", response_model=s.SubscriptionGet)
def read(subscription_id: int):
    return service.get(subscription_id)


@router.post("", response_model=s.SubscriptionGet)
def create(payload: s.SubscriptionCreate):
    subscription = service.create(payload)
    return subscription


@router.get("", response_model=t.List[s.SubscriptionGet])
def index():
    return service.get_list()
