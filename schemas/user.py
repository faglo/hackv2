from pydantic import BaseModel
from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional
from models import UserModel
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


class UserFilter(Filter):
    id: Optional[int]
    is_admin: Optional[bool]
    telegram_id: Optional[int]
    first_name: Optional[str]
    username: Optional[str]
    client: Optional[str]
    created_at: Optional[str]

    class Constants(Filter.Constants):
        model = UserModel
