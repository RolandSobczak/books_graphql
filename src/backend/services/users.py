from datetime import datetime, timedelta
from typing import Type

from jose import jwt
from passlib.context import CryptContext

from backend.models import UserModel
from backend.services.base import BaseService


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService(BaseService):

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    @classmethod
    def create_access_token(cls, data: dict):
        expire = datetime.utcnow() + timedelta(seconds=cls._settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        data.update({"exp": expire})
        return jwt.encode(data, cls._settings.SECRET_KEY, algorithm=cls._settings.ALGORITHM)

    @classmethod
    def decode_access_token(cls, token: str) -> UserModel:
        payload = jwt.decode(token, cls._settings.SECRET_KEY, algorithms=[cls._settings.ALGORITHM])
        return payload

    def get_user_by_username(self, username: str) -> Type[UserModel] | None:
        return self.db.query(UserModel).filter(UserModel.username == username).first()
