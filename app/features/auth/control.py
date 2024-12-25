from ..util.database import get_edgedb_client, handle_database_errors
from fastapi import Depends, Request
from ..Model.preAccess import Register
from ..Model.preAccess import Login

@handle_database_errors
async def register(
    request: Request,
    data: Register,
    hashed_password: str,
    db = Depends(get_edgedb_client)
):
    from app.queries.create_user_async_edgeql import create_user
    await create_user(
        executor=db,
        email=data.email,
        name=data.name,
        password=hashed_password,
    )
    return {
        "status": "success",
        "message": "Client created successfully!"
    }

@handle_database_errors
async def login(
    request: Request,
    data: Login,
    db = Depends(get_edgedb_client)
):
    from ..queries.login_user_async_edgeql import login_user, LoginUserResult
    result: LoginUserResult = await login_user(
        executor=db,
        email=data.email
    )
    return result