from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from backend.settings import Settings

settings = Settings()


SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{settings.POSTGRES_CONFIG['USER']}:{settings.POSTGRES_CONFIG['PASSWORD']}"
    f"@/{settings.POSTGRES_CONFIG['DB']}?host={settings.POSTGRES_CONFIG['HOST']}&port={settings.POSTGRES_CONFIG['PORT']}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


class SessionManager:
    """Manage opened sessions.
    If session is already opened returns current session if not returns the newone.
    """

    _attributes = {}
    _session = None

    def __init__(self):
        self.__dict__ = self._attributes

        if self._session is None:
            self.open_new_session()

    def __del__(self):
        self._session.close()

    def open_new_session(self):
        self._session = SessionLocal()

    @property
    def session(self):
        return self._session
