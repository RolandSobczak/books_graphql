from typing import List, Type

from backend.services.base import BaseService
from backend.models import BookModel


class BookService(BaseService):

    def get_all_books(self, *query) -> List[Type[BookModel]]:
        return self.db.query(BookModel).all()

    def get_book_by_id(self, book_id) -> Type[BookModel] | None:
        return self.db.query(BookModel).filter(BookModel.id == book_id).first()