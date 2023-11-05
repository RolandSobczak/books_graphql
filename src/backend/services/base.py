from abc import ABC

from sqlalchemy.orm import Session

from backend.db import SessionManager
from backend.settings import Settings


class BaseService(ABC):
    _manager = SessionManager()
    _settings = Settings()

    def __init__(self):
        self.db: Session = self._manager.session
