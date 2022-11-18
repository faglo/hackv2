from sqlalchemy.orm import sessionmaker
from database import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_database_connection():
    try:
        db = SessionLocal()
        yield db
        print("Connected to db")
    finally:
        db.close()
