from typing import Optional

from pydantic import BaseModel

class AuthorCreateSchema(BaseModel):
    first_name: str
    last_name: str


class AuthorUpdateSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
