from pydantic import BaseModel
from datetime import datetime


class UserSchema(BaseModel):
    id: int
    is_admin: bool
    telegram_id: int
    first_name: str
    username: str
    client: str
    created_at: datetime


class UserCreateSchema(BaseModel):
    telegram_id: int
    first_name: str
    username: str
    client: str

