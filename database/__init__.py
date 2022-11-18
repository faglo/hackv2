from config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    DATABASE_URL,
    echo=True,
    future=True,
    pool_size=20,
    max_overflow=100,
)
Base = declarative_base(
    bind=engine,
)

