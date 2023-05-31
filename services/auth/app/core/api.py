from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from .settings import Settings
from ..routes import router


def create_app():
    app = FastAPI(
        title="Auth service",
    )
    settings = Settings()
    app.add_middleware(
        DBSessionMiddleware,
        db_url=settings.DB_CONNECTION_STRING,
        engine_args=dict(
            future=True,
            pool_size=10,
            pool_recycle=3600,
            pool_pre_ping=True,
        ),
        session_args=dict(future=True),
    )
    app.include_router(router)

    return app
