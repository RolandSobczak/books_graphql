from typing import Optional

from pydantic import BaseModel


class BookCreateSchema(BaseModel):
    title: str
    description: str
    author_id: int


class BookUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    author_id: Optional[int] = None
