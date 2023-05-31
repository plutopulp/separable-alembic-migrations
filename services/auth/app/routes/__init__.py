from fastapi import APIRouter

from .users import router as users_router

router = APIRouter(prefix="/auth")

router.include_router(users_router)
