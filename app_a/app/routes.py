from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return "This is app_a."


@router.get("/status")
def status():
    return {"alive": True}