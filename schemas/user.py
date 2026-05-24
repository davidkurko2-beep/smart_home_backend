from pydantic.v1 import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str
    full_name: str
