import strawberry

from fastapi import FastAPI, Depends
from strawberry.tools import merge_types
from strawberry.fastapi import GraphQLRouter

from backend.queries import BookQuery, AuthorQuery
from backend.services import BookService, AuthorService


async def get_context(
        book_service: BookService = Depends(BookService),
        author_service: AuthorService = Depends(AuthorService),
):
    return {
        "book_service": book_service,
        "author_service": author_service,
    }


all_queries = merge_types("AllQueries", (BookQuery, AuthorQuery))

schema = strawberry.Schema(query=all_queries)

graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
