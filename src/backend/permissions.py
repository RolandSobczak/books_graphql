import typing
import strawberry
from strawberry.permission import BasePermission
from strawberry.types import Info


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        current_user = info.context["current_user"]

        if current_user:
            return True
        return False


@strawberry.type
class Query:
    user: str = strawberry.field(permission_classes=[IsAuthenticated])