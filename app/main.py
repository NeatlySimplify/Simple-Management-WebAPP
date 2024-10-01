from http import HTTPStatus
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Depends, HTTPException
from .helper import get_token_header, get_query_token
from .View import (client,
                   finance,
                   helpmate,
                   scheduler,
                   service,
                   user)


templates = Jinja2Templates("../Static/templates")

app = FastAPI(dependencies=[Depends(get_query_token)])

list_router = [client, finance, helpmate, scheduler, service,user]
for item in list_router:
    app.include_router(item.router, prefix=f"/{item.__name__}")


app.get("/")
async def get_dashboard():
    return 0
