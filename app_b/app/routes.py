from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return "This is app_b."


@router.get("/status")
def status():
    return {"alive": True}
