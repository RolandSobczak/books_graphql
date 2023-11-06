import strawberry
from strawberry.types import Info

from backend.services.users import UserService, UserNotFoundException
from backend.schemas.users import UserCreateSchema
from backend.queries.users import User


@strawberry.type
class ErrorResponse:
    message: str = "Something went wrong"
    code: str = "INTERNAL_SERVER_ERROR"


@strawberry.type
class UserLoginResponse:
    access_token: str
    token_type: str


@strawberry.input
class LoginRequest:
    username: str
    password: str


LoginResultResponse = strawberry.union("LoginResultResponse", [UserLoginResponse, ErrorResponse])


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def login(self, info: Info, data: LoginRequest) -> LoginResultResponse:
        try:
            user_service: UserService = info.context["user_service"]
            user = user_service.login(**data.__dict__)

            access_token = user_service.create_access_token(
                data={"sub": user.username}
            )

            return UserLoginResponse(access_token=access_token, token_type="bearer")
        except UserNotFoundException as e:
            return ErrorResponse(message=str(e), code="UNAUTHORIZED")

    @strawberry.mutation
    async def register(self, info: Info, first_name: str, last_name: str, username: str, password: str) -> User:
        user_service: UserService = info.context["user_service"]

        user_data = UserCreateSchema(
            first_name=first_name,
            last_name=last_name,
            username=username,
            hashed_password=user_service.get_password_hash(password)
        )

        if user_service.get_user_by_username(username) is not None:
            raise Exception(f"User {username} already exists.")

        return user_service.create_user(user_data)
