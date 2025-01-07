from ..util.database import get_edgedb_client, handle_database_errors
from fastapi import Depends
from .model import Register
from .model import Login
from ...queries.auth.login_user_async_edgeql import login_user, LoginUserResult
from ...queries.auth.create_user_async_edgeql import create_user
from ..util.password import hash_password

@handle_database_errors
async def register(
    data: Register,
    db = Depends(get_edgedb_client)
):  
    data.password = hash_password(data.password)
    await create_user(
        executor=db,
        email=data.email,
        name=data.name,
        password=data.password,
    )
    return {
        "status": "success",
        "message": "Client created successfully!"
    }

@handle_database_errors
async def login(
    data: Login,
    db = Depends(get_edgedb_client)
) -> LoginUserResult:  
    result: LoginUserResult = await login_user(
        executor=db,
        email=data.email
    )
    return result