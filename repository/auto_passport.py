from models import AutoPassportModel
from schemas import AutoPassportSchema, AutoPassportCreateSchema
from repository.base import BaseRepository
from database.session import get_database_connection
from fastapi import UploadFile
from services.ocr_auto_passport import check_passport


class AutoPassportRepository(BaseRepository):
    async def create(self, auto_passport: AutoPassportCreateSchema):
        auto_passport = AutoPassportModel(**auto_passport.dict())
        self.database.add(auto_passport)
        self.database.commit()
        self.database.refresh(auto_passport)
        return auto_passport

    async def get_all(self):
        result = self.database.query(AutoPassportModel).all()
        return result

    async def update(self, id: int, auto_passport: AutoPassportSchema):
        passport = self.database.query(AutoPassportModel).filter(
            AutoPassportModel.id == id
        )
        passport.update(auto_passport.dict())
        self.database.commit()
        return passport.first()

    async def delete(self, id: int):
        auto_passport = (
            self.database.query(AutoPassportModel)
            .filter(AutoPassportModel.id == id)
            .delete()
        )
        await self.database.commit()
        return auto_passport

    async def validate_passport_id(self, passport_id: str):
        passport = (
            self.database.query(AutoPassportModel)
            .filter(AutoPassportModel.id == passport_id)
            .first()
        )
        passport.validated = True
        self.database.commit()
        self.database.refresh(passport)
        return passport

    async def check_passport_photo(self, file: UploadFile):
        text = await check_passport(file)
        datalines = []
        for line in text.splitlines():
            if line == "":
                continue
            datalines.append(line)

        auto_passport_id = None
        vin_id = None
        auto_model = None
        body_color = None
        engine_type = None
        i = 0
        print(datalines)
        for data in datalines:
            i += 1
            if ("У0" in data) and len(data) >= 9 and auto_passport_id is None:
                auto_passport_id = data.replace(".", "").strip().replace(".", "")
            if ("1. " in data) and len(data) >= 9 and vin_id is None:
                vin_id = datalines[i].strip()
            if ("2. " in data) and len(data) >= 9 and auto_model is None:
                auto_model = datalines[i].strip()
            if ("9. " in data) and len(data) >= 9 and body_color is None:
                body_color = data.split(" ")[-1].strip()
            if ("12. " in data) and len(data) >= 9 and engine_type is None:
                engine_type = data.split(" ")[-1].strip()

        return dict(
            passport_id=auto_passport_id,
            vin_id=vin_id,
            auto_model=auto_model,
            body_color=body_color,
            engine_type=engine_type,
        )


def get_auto_passport_service() -> AutoPassportRepository:
    db = get_database_connection()
    return AutoPassportRepository(next(db))
