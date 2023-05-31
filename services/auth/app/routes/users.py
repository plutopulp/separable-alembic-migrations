import typing as t

from app.schemas import users as s
from app.services import users as service
from fastapi.routing import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}", response_model=s.UserGet)
def read(user_id: int):
    return service.get(user_id)


@router.post("", response_model=s.UserGet)
def create(payload: s.UserCreate):
    user = service.create(payload)
    return user


@router.get("", response_model=t.List[s.UserGet])
def index():
    return service.get_list()
