from fastapi import APIRouter, Depends
from repository import (
    UserRepository,
    get_user_service,
)
from schemas import (
    UserSchema,
    UserCreateSchema,
    UserFilter,
)
from tasks.worker import send_message_to_holder_channel
from fastapi_filter import FilterDepends

holder_router = APIRouter()

SUCCESS = {"status": "success"}


def make_valid_resp(data, schema):
    return [schema(**obj.__dict__) for obj in data]


@holder_router.get("/accounts", response_model=list[AccountSchema])
async def get_accounts(
    account_service: AccountRepository = Depends(get_account_service),
    account_filter: AccountFilter = FilterDepends(AccountFilter),
):
    accounts = await account_service.get_all(account_filter)
    return make_valid_resp(accounts, AccountSchema)


@holder_router.post("/accounts", response_model=AccountSchema)
async def create_account(
    account: AccountCreateSchema,
    account_service: AccountRepository = Depends(get_account_service),
):
    acc = await account_service.create(account)
    return AccountSchema(**acc.__dict__)


@holder_router.put("/accounts/{account_id}", response_model=AccountSchema)
async def update_account(
    account_id: int,
    account: AccountSchema,
    account_service: AccountRepository = Depends(get_account_service),
):
    acc = await account_service.update(account_id, account)
    return AccountSchema(**acc.__dict__)


@holder_router.delete("/accounts/{account_id}", response_model=dict)
async def delete_account(
    account_id: int,
    account_service: AccountRepository = Depends(get_account_service),
):
    await account_service.delete(account_id)
    return SUCCESS


@holder_router.get("/orders", response_model=list[OrderSchema])
async def get_orders(
    order_service: OrderRepository = Depends(get_order_service),
    order_filter: OrderFilter = FilterDepends(OrderFilter),
):
    orders = await order_service.get_all(order_filter)
    return make_valid_resp(orders, OrderSchema)


@holder_router.post("/orders", response_model=OrderSchema)
async def create_order(
    order: OrderCreateSchema,
    order_service: OrderRepository = Depends(get_order_service),
):
    ordr = await order_service.create(order)
    return OrderSchema(**ordr.__dict__)


@holder_router.put("/orders/{order_id}", response_model=OrderSchema)
async def update_order(
    order_id: int,
    order: OrderSchema,
    order_service: OrderRepository = Depends(get_order_service),
):
    ordr = await order_service.update(order_id, order)
    return OrderSchema(**ordr.__dict__)


@holder_router.delete("/orders/{order_id}", response_model=dict)
async def delete_order(
    order_id: int,
    order_service: OrderRepository = Depends(get_order_service),
):
    await order_service.delete(order_id)
    return SUCCESS


@holder_router.get("/users", response_model=list[UserSchema])
async def get_users(
    user_service: UserRepository = Depends(get_user_service),
    user_filter: UserFilter = FilterDepends(UserFilter),
):
    users = await user_service.get_all(user_filter)
    return make_valid_resp(users, UserSchema)


@holder_router.post("/users", response_model=UserSchema)
async def create_user(
    user: UserCreateSchema,
    user_service: UserRepository = Depends(get_user_service),
):
    usr = await user_service.create(user)
    return UserSchema(**usr.__dict__)


@holder_router.put("/users/{user_id}", response_model=UserSchema)
async def update_user(
    user_id: int,
    user: UserSchema,
    user_service: UserRepository = Depends(get_user_service),
):
    usr = await user_service.update(user_id, user)
    return UserSchema(**usr.__dict__)


@holder_router.delete("/users/{user_id}", response_model=dict)
async def delete_user(
    user_id: int,
    user_service: UserRepository = Depends(get_user_service),
):
    await user_service.delete(user_id)
    return SUCCESS


@holder_router.get("/transactions", response_model=list[TransactionSchema])
async def get_transactions(
    transaction_service: TransactionRepository = Depends(get_transaction_service),
    transaction_filter: TransactionFilter = FilterDepends(TransactionFilter),
):
    transactions = await transaction_service.get_all(transaction_filter)
    return make_valid_resp(transactions, TransactionSchema)


@holder_router.post("/transactions", response_model=TransactionSchema)
async def create_transaction(
    transaction: TransactionCreateSchema,
    transaction_service: TransactionRepository = Depends(get_transaction_service),
):
    trx = await transaction_service.create(transaction)
    return TransactionSchema(**trx.__dict__)


@holder_router.put("/transactions/{transaction_id}", response_model=TransactionSchema)
async def update_transaction(
    transaction_id: int,
    transaction: TransactionSchema,
    transaction_service: TransactionRepository = Depends(get_transaction_service),
):
    trx = await transaction_service.update(transaction_id, transaction)
    return TransactionSchema(**trx.__dict__)


@holder_router.delete("/transactions/{transaction_id}", response_model=dict)
async def delete_transaction(
    transaction_id: int,
    transaction_service: TransactionRepository = Depends(get_transaction_service),
):
    await transaction_service.delete(transaction_id)
    return SUCCESS


@holder_router.post("/send_actualize_message/")
def send_actualize_message():
    send_message_to_holder_channel.delay("Актуализируйте балансы!", "alfabit")
    return SUCCESS
