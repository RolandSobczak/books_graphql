from datetime import datetime
from typing import TYPE_CHECKING, Annotated
import strawberry
from strawberry.types import Info

from backend.services import BookService


if TYPE_CHECKING:
    from backend.queries.authors import Author


@strawberry.type
class Book:
    id: int
    title: str
    description: str
    author: Annotated["Author", strawberry.lazy(".authors")]
    created_at: datetime
    updated_at: datetime


@strawberry.type
class BookQuery:
    @strawberry.field
    async def books(self, info: Info) -> list[Book]:
        book_service: BookService = info.context["book_service"]

        books = book_service.get_all_books()
        return books

    @strawberry.field
    async def book(self, info: Info, book_id: int) -> Book | None:
        book_service: BookService = info.context["book_service"]

        book = book_service.get_book_by_id(book_id)
        return book
