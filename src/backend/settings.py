import logging
from functools import lru_cache

from environs import Env
from pydantic_settings import BaseSettings

env = Env()


class Settings(BaseSettings):
    LOG_LEVEL: int = env.log_level("LOG_LEVEL", logging.INFO)
    MAX_PER_PAGE: int = env.int("MAX_PER_PAGE", 20)

    SECRET_KEY: str = env("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_SECONDS: int = env.int("ACCESS_TOKEN_EXPIRE_SECONDS", 3600)
    ALGORITHM: str = env("ALGORITHM", "HS256")

    POSTGRES_CONFIG: dict = {
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT", default="5432"),
        "DB": env("POSTGRES_DB"),
    }
