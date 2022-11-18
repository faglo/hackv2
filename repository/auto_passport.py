from models import AutoPassportModel
from schemas import AutoPassportSchema, AutoPassportCreateSchema
from repository.base import BaseRepository
from database.session import get_database_connection


class AutoPassportRepository(BaseRepository):
    async def create(self, auto_passport: AutoPassportCreateSchema):
        auto_passport = AutoPassportCreateSchema(**auto_passport.dict())
        self.database.add(auto_passport)
        self.database.commit()
        self.database.refresh(auto_passport)
        return auto_passport

    async def get_all(self):
        result = self.database.query(AutoPassportModel).all()
        return result

    async def update(self, id: int, auto_passport: AutoPassportSchema):
        passport = (
            self.database.query(AutoPassportModel)
            .filter(AutoPassportModel.id == id)
            .update(auto_passport.dict())
        )
        await self.database.commit()
        return passport

    async def delete(self, id: int):
        auto_passport = (
            self.database.query(AutoPassportModel)
            .filter(AutoPassportModel.id == id)
            .delete()
        )
        await self.database.commit()
        return auto_passport


def get_auto_passport_service() -> AutoPassportRepository:
    db = get_database_connection()
    return AutoPassportRepository(next(db))
