from datetime import datetime
from typing import List, TYPE_CHECKING, Annotated

import strawberry
from strawberry.types import Info

from backend.services import AuthorService, BookService
from backend.models import BookModel

if TYPE_CHECKING:
    from backend.queries.books import Book


@strawberry.type
class Author:
    id: int
    first_name: str
    last_name: str
    books: List[Annotated["Book", strawberry.lazy(".books")]]
    created_at: datetime
    updated_at: datetime


@strawberry.type
class AuthorQuery:

    @strawberry.field
    async def authors(self, info: Info) -> list[Author]:
        author_service: AuthorService = info.context["author_service"]

        authors = author_service.get_all_authors()
        return authors

    @strawberry.field
    async def author(self, info: Info, author_id: int) -> Author:
        author_service: AuthorService = info.context["author_service"]

        author = author_service.get_author_by_id(author_id)
        return author