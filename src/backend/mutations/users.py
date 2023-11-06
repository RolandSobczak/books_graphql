import strawberry
from strawberry.types import Info

from backend.services.users import UserService, UserNotFoundException


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
