from sqlalchemy.orm import Session
from abc import ABC, abstractmethod


class BaseRepository(ABC):
    def __init__(self, database: Session):
        self.database = database

    @abstractmethod
    def create(*args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def get_all():
        raise NotImplementedError()

    @abstractmethod
    def update(*args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def delete(*args, **kwargs):
        raise NotImplementedError()
