from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func


class AutoPassport(Base):
    __tablename__ = "auto_passports"
    id = Column(Integer, primary_key=True)
    vin_id = Column(String, nullable=False)
    auto_model = Column(String, nullable=False)
    auto_type = Column(String, nullable=False)
    auto_category = Column(String, nullable=False)
    auto_created_year = Column(Integer, nullable=False)
    engine_model = Column(String, nullable=False)
    engine_id = Column(String, nullable=False)
    chasis_id = Column(String, nullable=False)
    body_id = Column(String, nullable=False)
    body_color = Column(String, nullable=False)
    engine_power = Column(String, nullable=False)
    engine_value = Column(Integer, nullable=False)
    engine_type = Column(String, nullable=False)
    ecological_class = Column(String, nullable=False)
    max_weight = Column(Integer, nullable=False)
    min_weight = Column(Integer, nullable=False)
    auto_maker = Column(String, nullable=False)
    auto_maker_country = Column(String, nullable=False)
    auto_accept_type = Column(String, nullable=False)
    auto_accept_date = Column(String, nullable=False)
    auto_from_country = Column(String, nullable=False)
    customs_declaration_id = Column(String, nullable=False)
    customs_restrictions = Column(String, nullable=False)
    auto_owner = Column(String, nullable=False)
    auto_adress = Column(String, nullable=False)
    who_issued = Column(String, nullable=False)
    issued_address = Column(String, nullable=False)
    issued_at = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
