from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from backend.settings import Settings


Base = declarative_base()


class SessionManager:
    """Manage opened sessions.
    If session is already opened returns current session if not returns the newone.
    """

    _attributes: dict = {}
    _settings: Settings = Settings()
    _engine = None
    _session = None

    def __init__(self):
        self.__dict__ = self._attributes

        if self._session is None:
            self._open_new_session()

    def __del__(self):
        self._session.close()

    def _open_new_connection(self):
        sqlalchemy_db_url = (
            f"postgresql+psycopg2://{self._settings.POSTGRES_CONFIG['USER']}:{self._settings.POSTGRES_CONFIG['PASSWORD']}"
            f"@/{self._settings.POSTGRES_CONFIG['DB']}?host={self._settings.POSTGRES_CONFIG['HOST']}&port={self._settings.POSTGRES_CONFIG['PORT']}"
        )
        return create_engine(sqlalchemy_db_url)

    def _open_new_session(self):
        if self._engine is None:
            self._open_new_connection()

        session_local = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self._engine,
        )
        self._session = session_local()

    @property
    def session(self) -> Session:
        return self._session
