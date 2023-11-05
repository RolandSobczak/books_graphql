from typing import List, Type

from backend.services.base import BaseService
from backend.models import AuthorModel, BookModel


class AuthorService(BaseService):

    def get_all_authors(self, *query) -> List[Type[AuthorModel]]:
        return self.db.query(AuthorModel).join(BookModel).filter(*query).all()

    def get_author_by_id(self, author_id: int) -> Type[AuthorModel] | None:
        return self.db.query(AuthorModel).filter(AuthorModel.id == author_id).first()