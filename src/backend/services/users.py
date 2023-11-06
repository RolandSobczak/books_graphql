from datetime import datetime, timedelta
from typing import Type

from jose import jwt
from passlib.context import CryptContext

from backend.models import UserModel
from backend.schemas.users import UserCreateSchema
from backend.services.base import BaseService


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserNotFoundException(Exception):
    pass


class UserService(BaseService):

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    @classmethod
    def create_access_token(cls, data: dict):
        expire = datetime.utcnow() + timedelta(seconds=cls._settings.ACCESS_TOKEN_EXPIRE_SECONDS)
        data.update({"exp": expire})
        return jwt.encode(data, cls._settings.SECRET_KEY, algorithm=cls._settings.ALGORITHM)

    @classmethod
    def decode_access_token(cls, token: str) -> dict:
        payload = jwt.decode(token, cls._settings.SECRET_KEY, algorithms=[cls._settings.ALGORITHM])
        return payload

    def get_user_by_username(self, username: str) -> Type[UserModel] | None:
        return self.db.query(UserModel).join(UserModel.saved_books, isouter=True).filter(UserModel.username == username).first()

    def login(self, username: str, password: str) -> Type[UserModel]:
        user = self.get_user_by_username(username)

        if user is None:
            raise UserNotFoundException("Username or password is invalid")

        if not self.verify_password(password, user.hashed_password):
            raise UserNotFoundException("Username or password is invalid")

        return user

    def create_user(self, user_data: UserCreateSchema) -> Type[UserModel]:
        user = UserModel(**user_data.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
