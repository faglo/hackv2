from fastapi import APIRouter, Depends
from repository import (
    UserRepository,
    get_user_service,
)
from schemas import (
    UserSchema,
    UserCreateSchema,
)

router = APIRouter()

SUCCESS = {"status": "success"}


def make_valid_resp(data, schema):
    return [schema(**obj.__dict__) for obj in data]



@router.get("/users", response_model=list[UserSchema])
async def get_users(
    user_service: UserRepository = Depends(get_user_service),
):
    users = await user_service.get_all()
    return make_valid_resp(users, UserSchema)


@router.post("/users", response_model=UserSchema)
async def create_user(
    user: UserCreateSchema,
    user_service: UserRepository = Depends(get_user_service),
):
    usr = await user_service.create(user)
    return UserSchema(**usr.__dict__)


@router.put("/users/{user_id}", response_model=UserSchema)
async def update_user(
    user_id: int,
    user: UserSchema,
    user_service: UserRepository = Depends(get_user_service),
):
    usr = await user_service.update(user_id, user)
    return UserSchema(**usr.__dict__)


@router.delete("/users/{user_id}", response_model=dict)
async def delete_user(
    user_id: int,
    user_service: UserRepository = Depends(get_user_service),
):
    await user_service.delete(user_id)
    return SUCCESS
