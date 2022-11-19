from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ARRAY
from sqlalchemy.sql import func


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    is_admin = Column(Boolean, server_default="false")
    first_name = Column(String(50), nullable=False)
    second_name = Column(String(50), nullable=False)
    third_name = Column(String(50), nullable=False)
    esia_id = Column(String, nullable=True)
    auto_passport_ids = Column(ARRAY(String), server_default="{}")
    created_at = Column(DateTime, server_default=func.now())
