from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTION_STRING: str
    DB_SCHEMA_AUTH: str
    DB_SCHEMA_BILLING: str
    DB_CREATE_TABLES: int


@lru_cache()
def get_settings() -> Settings:
    return Settings()  # type: ignore
