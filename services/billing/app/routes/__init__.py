from fastapi import APIRouter

from .subscriptions import router as subscriptions_router
from .user_subscriptions import router as user_subscriptions_router

router = APIRouter(prefix="/auth")

router.include_router(subscriptions_router)
router.include_router(user_subscriptions_router)
