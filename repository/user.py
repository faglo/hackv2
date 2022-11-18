from models import UserModel
from schemas import UserSchema, UserCreateSchema
from repository.base import BaseRepository
from database.session import get_database_connection


class UserRepository(BaseRepository):
    async def create(self, user: UserCreateSchema):
        user = UserModel(**user.dict())
        self.database.add(user)
        self.database.commit()
        self.database.refresh(user)
        return user

    async def get_all(self):
        users = self.database.query(UserModel).all()
        return users

    async def update(self, id: int, user: UserSchema):
        user = (
            self.database.query(UserModel)
            .filter(UserModel.id == id)
            .update(user.dict())
        )
        await self.database.commit()
        return user

    async def delete(self, id: int):
        user = self.database.query(UserModel).filter(UserModel.id == id).delete()
        await self.database.commit()
        return user


def get_user_service() -> UserRepository:
    db = get_database_connection()
    return UserRepository(next(db))
