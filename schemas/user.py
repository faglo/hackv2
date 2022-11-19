from pydantic import BaseModel
from datetime import datetime


class UserSchema(BaseModel):
    id: int
    is_admin: bool
    first_name: str
    second_name: str
    third_name: str
    esia_id: str
    auto_passport_ids: list
    created_at: datetime


class UserCreateSchema(BaseModel):
    first_name: str
    second_name: str
    third_name: str
    esia_id: str
