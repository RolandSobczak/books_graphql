import logging
from functools import lru_cache

from environs import Env
from pydantic_settings import BaseSettings

env = Env()


class Settings(BaseSettings):
    LOG_LEVEL = env.log_level("LOG_LEVEL", logging.INFO)
    MAX_PER_PAGE = env.int("MAX_PER_PAGE", 20)

    CORS_CONFIG = {
        "ALLOWED_ORIGINS": env.list("ALLOWED_ORIGINS"),
        "ALLOW_CREDENTIALS": env.bool("ALLOW_CREDENTIALS"),
        "ALLOWED_METHODS": env.list("ALLOWED_METHODS"),
        "ALLOWED_HEADERS": env.list("ALLOWED_HEADERS"),
    }

    POSTGRES_CONFIG = {
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT", default="5432"),
        "DB": env("POSTGRES_DB"),
    }
