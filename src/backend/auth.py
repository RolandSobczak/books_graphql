import logging

from jose import JWTError

from backend.services import UserService
from backend.models import UserModel


def get_current_user(
        token: str,
        user_service: UserService
) -> UserModel | None:
    try:
        payload = user_service.decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            logging.debug("JWT Token doesn't contain username.")
        user = user_service.get_user_by_username(username)
        if user is None:
            logging.debug(f"User with provided username does not exist. [username={username}]")

        return user

    except JWTError:
        logging.debug("Invalid JWT token.")
        return None
