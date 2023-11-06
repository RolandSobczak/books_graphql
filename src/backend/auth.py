from jose import JWTError

from backend.services import UserService
from backend.models import UserModel


class UserNotAuthorizedException(Exception):
    pass


def get_current_user(
        token: str,
        user_service: UserService
) -> UserModel:
    credentials_exception = UserNotAuthorizedException("Could not validate credentials")

    try:
        payload = user_service.decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = user_service.get_user_by_username(username)
    # if user is None:
    #     raise credentials_exception

    return user
