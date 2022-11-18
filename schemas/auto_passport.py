from pydantic import BaseModel
from datetime import datetime


class AutoPassportSchema(BaseModel):
    id: int
    vin_id: str
    auto_model: str
    auto_type: str
    auto_category: str
    auto_created_year: int
    engine_model: str
    engine_id: str
    chasis_id: str
    body_id: str
    body_color: str
    engine_power: str
    engine_value: int
    engine_type: str
    ecological_class: str
    max_weight: int
    min_weight: int
    auto_maker: str
    auto_maker_country: str
    auto_accept_type: str
    auto_accept_date: str
    auto_from_country: str
    customs_declaration_id: str
    customs_restrictions: str
    auto_owner: str
    auto_adress: str
    who_issued: str
    issued_address: str
    issued_at: str
    created_at: datetime


class AutoPassportCreateSchema(BaseModel):
    vin_id: str
    auto_model: str
    auto_type: str
    auto_category: str
    auto_created_year: int
    engine_model: str
    engine_id: str
    chasis_id: str
    body_id: str
    body_color: str
    engine_power: str
    engine_value: int
    engine_type: str
    ecological_class: str
    max_weight: int
    min_weight: int
    auto_maker: str
    auto_maker_country: str
    auto_accept_type: str
    auto_accept_date: str
    auto_from_country: str
    customs_declaration_id: str
    customs_restrictions: str
    auto_owner: str
    auto_adress: str
    who_issued: str
    issued_address: str
    issued_at: str
