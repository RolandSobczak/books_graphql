from sqlalchemy import String, Table, ForeignKey, Column, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.db import Base


user_saved_books = Table(
    "user_saved_books",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("book_id", ForeignKey("books.id")),
)
unique_together_constraint = UniqueConstraint('user_id', 'book_id', name='uq_user_saved_books')
user_saved_books.append_constraint(unique_together_constraint)


class UserModel(Base):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("username"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255))
    hashed_password: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    saved_books: Mapped[list["BookModel"]] = relationship(secondary=user_saved_books, back_populates="followers")
