from typing import Optional

import strawberry
from strawberry.types import Info

from backend.schemas.author import AuthorUpdateSchema, AuthorCreateSchema
from backend.queries.authors import Author
from backend.services import AuthorService

@strawberry.type
class AuthorMutation:

    @strawberry.mutation
    async def add_author(self, info: Info, first_name: str, last_name: str) -> Author:
        author_service: AuthorService = info.context["author_service"]

        author = AuthorCreateSchema(first_name=first_name, last_name=last_name)

        return author_service.insert_author(author)

    @strawberry.mutation
    async def update_author(self, info: Info, author_id: int, first_name: Optional[str] = None, last_name: Optional[str] = None) -> Author | None:
        author_service: AuthorService = info.context["author_service"]

        author = AuthorUpdateSchema(first_name=first_name, last_name=last_name)

        return author_service.update_author(author_id, author)

    @strawberry.mutation
    async def delete_author(self, info: Info, author_id: int) -> None:
        author_service: AuthorService = info.context["author_service"]

        return author_service.delete_author(author_id)

