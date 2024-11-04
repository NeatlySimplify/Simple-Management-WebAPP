
from http import HTTPStatus
from http.client import NOT_FOUND

from fastapi import HTTPException
from httpx import HTTPError, HTTPStatusError
from app.queries import (
    create_user_async_edgeql as create_user,
    create_userBankAccount_async_edgeql as create_bankAccount,
    delete_userBankAccount_async_edgeql as delete_bankAccount,
    login_user_async_edgeql as login_user,
    read_user_async_edgeql as retrieve_user,
    update_user_async_edgeql as update_user,
    delete_user_async_edgeql as delete_user,
    update_userBankAccount_async_edgeql as update_bankAccount
)

from . import *
import bcrypt
from app.Model.people import User, Login


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password, bcrypt.gensalt())


def compare_password(hashed, password) -> bool:
    return bcrypt.checkpw(password, hashed)


async def create_user(user: User):
    hashed_password = hash_password(user.password)
    await create_user_async_edgeql.create_user(
        executor=db_async_client,
        email=user.email,
        nome=user.nome,
        sexo=user.sexo,
        estado_civil=user.estado_civil,
        details=user.details,
        tag_tipo=user.tag_tipo,
        nascimento=user.nascimento,
        password=hashed_password,
    )

async def login(login: Login, user: User):
    try:
        result = await login_user.login_user(
        executor=db_async_client,
        email=login.email
        )
        user = User.model_validate_json(result)
        validate = compare_password(user.password, login.password)
        if not result:
            return Exception(NOT_FOUND)
        elif not validate:
            pass
        else:
            return user
    except edgedb.errors.ClientConnectionError:
        raise HTTPException(503)

async def register():
    user = await retrieve_user.read_user(
        executor=db_async_client,

        )
