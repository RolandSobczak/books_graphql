from typing import List

from sqlalchemy import String, ForeignKey, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.db import Base
from backend.models.mixins import TimestampedMixin
from backend.models.users import  user_saved_books


class BookModel(Base, TimestampedMixin):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["AuthorModel"] = relationship(back_populates="books")
    followers: Mapped[List["UserModel"]] = relationship(secondary=user_saved_books, back_populates="saved_books")


