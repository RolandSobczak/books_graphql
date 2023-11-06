from datetime import datetime
from typing import TYPE_CHECKING, Annotated, List
import strawberry
from strawberry.types import Info

from backend.services import UserService
from backend.permissions import IsAuthenticated


if TYPE_CHECKING:
    from backend.queries.books import Book


@strawberry.type
class User:
    id: int
    username: str
    first_name: str
    last_name: str
    saved_books: List[Annotated["Book", strawberry.lazy(".books")]]


@strawberry.type
class UserQuery:

    @strawberry.field(permission_classes=[IsAuthenticated])
    async def current_user(self, info: Info) -> User:
        current_user: UserService = info.context["current_user"]

        return current_user
