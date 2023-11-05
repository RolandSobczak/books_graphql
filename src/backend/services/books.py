from typing import List, Type

from sqlalchemy import update

from backend.services.base import BaseService
from backend.models import BookModel
from backend.schemas.books import BookCreateSchema, BookUpdateSchema


class BookService(BaseService):

    def get_all_books(self, *query) -> List[Type[BookModel]]:
        return self.db.query(BookModel).all()

    def get_book_by_id(self, book_id) -> Type[BookModel] | None:
        return self.db.query(BookModel).filter(BookModel.id == book_id).first()

    def insert_book(self, book: BookCreateSchema) -> BookModel:
        new_book = BookModel(**book.model_dump())
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        return new_book

    def update_book(self, book_id: int, book: BookUpdateSchema) -> BookModel:
        book = self.db.execute(
            update(BookModel)
            .where(BookModel.id == book_id)
            .values(**book.model_dump(exclude_none=True))
            .returning(BookModel)
        )
        return book.scalar()

    def delete_book(self, book_id: int) -> None:
        self.db.query(BookModel).filter(BookModel.id == book_id).delete()