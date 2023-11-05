from typing import List, Type

from sqlalchemy import update

from backend.services.base import BaseService
from backend.schemas.author import AuthorUpdateSchema, AuthorCreateSchema
from backend.models import AuthorModel, BookModel


class AuthorService(BaseService):

    def get_all_authors(self, *query) -> List[Type[AuthorModel]]:
        return self.db.query(AuthorModel).join(BookModel).filter(*query).all()

    def get_author_by_id(self, author_id: int) -> Type[AuthorModel] | None:
        return self.db.query(AuthorModel).filter(AuthorModel.id == author_id).first()

    def insert_author(self, author: AuthorCreateSchema) -> AuthorModel:
        new_author = AuthorModel(**author.model_dump(exclude_none=True))
        self.db.add(new_author)
        self.db.commit()
        self.db.refresh(new_author)
        return new_author

    def update_author(self, author_id: int, author: AuthorUpdateSchema) -> AuthorModel:
        author = self.db.execute(
            update(AuthorModel)
            .where(AuthorModel.id == author_id)
            .values(**author.model_dump(exclude_none=True))
            .returning(AuthorModel)
        )
        return author.scalar()

    def delete_author(self, author_id: int) -> None:
        self.db.query(AuthorModel).filter(AuthorModel.id == author_id).delete()
