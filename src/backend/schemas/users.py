from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    hashed_password: str
