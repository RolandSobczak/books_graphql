import strawberry

from fastapi import FastAPI, Depends, Request
from strawberry.tools import merge_types
from strawberry.fastapi import GraphQLRouter

from backend.queries import BookQuery, AuthorQuery, UserQuery
from backend.mutations import BookMutation, AuthorMutation, UserMutation
from backend.services import BookService, AuthorService, UserService
from backend.auth import get_current_user


async def get_context(
    request: Request,
    book_service: BookService = Depends(BookService),
    author_service: AuthorService = Depends(AuthorService),
    user_service: UserService = Depends(UserService),
):
    authorization = request.headers.get("Authorization", "")
    token = authorization.replace("Bearer ", "")

    context = {
        "book_service": book_service,
        "author_service": author_service,
        "user_service": user_service,
        "current_user": None
    }
    if token:
        context.update({"current_user": get_current_user(token, user_service),})

    return context


all_queries = merge_types("AllQueries", (BookQuery, AuthorQuery, UserQuery))
all_mutations = merge_types("AllMutations", (BookMutation, AuthorMutation, UserMutation))

schema = strawberry.Schema(query=all_queries, mutation=all_mutations)

graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
