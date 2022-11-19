from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func


class AutoPassportModel(Base):
    __tablename__ = "auto_passports"
    id = Column(Integer, primary_key=True)
    passport_id = Column(String, nullable=False)
    vin_id = Column(String, nullable=False)
    auto_model = Column(String, nullable=False)
    body_color = Column(String, nullable=False)
    engine_type = Column(String, nullable=False)
    validated = Column(Boolean, server_default="false")
    created_at = Column(DateTime, server_default=func.now())
