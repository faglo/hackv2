from fastapi import APIRouter, Depends, UploadFile, File
from repository import (
    UserRepository,
    get_user_service,
    AutoPassportRepository,
    get_auto_passport_service,
)
from schemas import (
    UserSchema,
    UserCreateSchema,
    AutoPassportSchema,
    AutoPassportCreateSchema,
)

router = APIRouter()

SUCCESS = {"status": "success"}


def make_valid_resp(data, schema):
    return [schema(**obj.__dict__) for obj in data]


# PASS
@router.get("/users", response_model=list[UserSchema])
async def get_users(
    user_service: UserRepository = Depends(get_user_service),
):
    users = await user_service.get_all()
    return make_valid_resp(users, UserSchema)


# PASS
@router.post("/users", response_model=UserSchema)
async def create_user(
    user: UserCreateSchema,
    user_service: UserRepository = Depends(get_user_service),
):
    usr = await user_service.create(user)
    return UserSchema(**usr.__dict__)


# PASS
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


# PASS
@router.get("/auto_passports", response_model=list[AutoPassportSchema])
async def get_auto_passports(
    passport_service: AutoPassportRepository = Depends(get_auto_passport_service),
):
    passports = await passport_service.get_all()
    return make_valid_resp(passports, AutoPassportSchema)


# PASS
@router.post("/auto_passports", response_model=AutoPassportSchema)
async def create_passport(
    passport: AutoPassportCreateSchema,
    passport_service: AutoPassportRepository = Depends(get_auto_passport_service),
):
    auto_passport = await passport_service.create(passport)
    return AutoPassportSchema(**auto_passport.__dict__)


# PASS
@router.put("/auto_passports/{passport_id}", response_model=AutoPassportSchema)
async def update_passport(
    passport_id: int,
    passport: AutoPassportSchema,
    passport_service: AutoPassportRepository = Depends(get_auto_passport_service),
):
    auto_passport = await passport_service.update(passport_id, passport)
    print(auto_passport)
    return AutoPassportSchema(**auto_passport.__dict__)


@router.delete("/auto_passports/{passports_id}", response_model=dict)
async def delete_passport(
    passport_id: int,
    passport_service: AutoPassportRepository = Depends(get_auto_passport_service),
):
    await passport_service.delete(passport_id)
    return SUCCESS


# PASS
@router.post(
    "/auto_passports/validate/{passport_id}", response_model=AutoPassportSchema
)
async def validate_passport(
    passport_id: int,
    passport_service: AutoPassportRepository = Depends(get_auto_passport_service),
):
    auto_passport = await passport_service.validate_passport_id(passport_id)
    return AutoPassportSchema(**auto_passport.__dict__)


@router.post("/auto_passports/upload")
async def upload_file(
    file: UploadFile = File(...),
    passport_service: AutoPassportRepository = Depends(get_auto_passport_service),
):
    return await passport_service.check_passport_photo(file=file)
