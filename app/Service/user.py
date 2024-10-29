from app.queries import create_user_async_edgeql, login_user_async_edgeql, read_user_async_edgeql

from ..queries import *
from . import *


async def login(user_email):
    user = await login_user_async_edgeql.login_user(
        executor=db_async_client,
        email=user_email
        )
    return user


async def register():
    user = await create_user_async_edgeql.create_user(
        executor=db_async_client,
        
    )
