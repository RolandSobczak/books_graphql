from typing import Optional

import strawberry
from strawberry.types import Info

from backend.schemas.books import BookCreateSchema, BookUpdateSchema
from backend.queries.books import Book
from backend.services import BookService
from backend.models import UserModel
from backend.permissions import IsAuthenticated


@strawberry.type
class BookMutation:

    @strawberry.mutation
    async def add_book(self, info: Info, title: str, description: str, author_id: int) -> Book:
        book_service: BookService = info.context["book_service"]

        book = BookCreateSchema(title=title, description=description, author_id=author_id)

        return book_service.insert_book(book)

    @strawberry.mutation
    async def update_book(self, info: Info, book_id: int, title: Optional[str] = None, description: Optional[str] = None, author_id: Optional[int] = None) -> Book | None:
        book_service: BookService = info.context["book_service"]

        book = BookUpdateSchema(title=title, description=description, author_id=author_id)

        return book_service.update_book(book_id, book)

    @strawberry.mutation
    async def delete_book(self, info: Info, book_id: int) -> None:
        book_service: BookService = info.context["book_service"]

        return book_service.delete_book(book_id)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def save_book(self, info: Info, book_id: int) -> Book | None:
        book_service: BookService = info.context["book_service"]
        current_user: UserModel = info.context["current_user"]

        return book_service.save_book(current_user, book_id)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def unsave_book(self, info: Info, book_id: int) -> Book | None:
        book_service: BookService = info.context["book_service"]
        current_user: UserModel = info.context["current_user"]

        book = book_service.get_book_by_id(book_id)
        if book not in current_user.saved_books:
            return None

        return book_service.unsave_book(current_user, book_id)



