from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from .routes import router

from .settings import Settings


def create_app(**config):
    app = FastAPI(title="App B")

    settings = Settings(**config)
    engine_args = dict()
    # Fine-tune the engine parameters if we're running against PostgreSQL
    if settings.DB_CONNECTION_STRING.startswith("postgresql://"):
        engine_args.update(dict(pool_size=25, pool_recycle=3600, pool_pre_ping=True))
    app.add_middleware(
        DBSessionMiddleware,
        db_url=settings.DB_CONNECTION_STRING,
        engine_args=engine_args,
    )
    # setup_database(create_tables=settings.DB_CREATE_TABLES)

    app.include_router(router)

    return app
