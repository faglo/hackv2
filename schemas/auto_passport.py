from pydantic import BaseModel
from datetime import datetime


class AutoPassportSchema(BaseModel):
    id: int
    passport_id: str
    vin_id: str
    auto_model: str
    body_color: str
    engine_type: str
    validated: bool
    created_at: datetime


class AutoPassportCreateSchema(BaseModel):
    passport_id: str
    vin_id: str
    auto_model: str
    body_color: str
    engine_type: str
