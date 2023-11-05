from typing import List

from sqlalchemy import String, ForeignKey, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.db import Base
from backend.models.mixins import TimestampedMixin


class BookModel(Base, TimestampedMixin):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["AuthorModel"] = relationship(back_populates="books")

