from typing import List

from sqlalchemy import String, ForeignKey, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.db import Base
from backend.models.mixins import TimestampedMixin


class AuthorModel(Base, TimestampedMixin):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    books: Mapped[List["BookModel"]] = relationship(back_populates="author")
