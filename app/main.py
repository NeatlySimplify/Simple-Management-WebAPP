
from pathlib import Path
from http import HTTPStatus
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.staticfiles import StaticFiles
import asyncio
#from .View import (client,
                #    finance,
                #    scheduler,
                #    service,
                #    user)

now_path = str(Path.cwd())

app = FastAPI()
top = Path(__file__).resolve().parent
app.mount("/Static", StaticFiles(directory=f"{now_path}/app/Static"), name="Static")


templates = Jinja2Templates(directory=f"{top}/Static/templates")


#list_router = [client, finance, scheduler, service,user]
#for item in list_router:
#    app.include_router(item.router, prefix=f"/{item.__name__}")


item = [
    {
        "id": "3325rwar23xaxsxaxs",
        "date_end": "12/11/3411",
        "origem": "Finance",
        "name": "Contas"
    },
    {
        "id": "3325rwar23xaxsxaxs",
        "date_end": "12/11/3411",
        "origem": "Finance",
        "name": "Contas"
    },
    {
        "id": "3325rwar23xaxsxaxs",
        "date_end": "12/11/3411",
        "origem": "Finance",
        "name": "Contas"
    },
    {
        "id": "3325rwar23xaxsxaxs",
        "date_end": "12/11/3411",
        "origem": "Finance",
        "name": "Contas"
    }
]

@app.get("/")
async def get_dashboard(request: Request):
    return templates.TemplateResponse( 
        "dashboard.html", 
        {
            "request": request,
            "cliente_num": 14,
            "service_num": 7,
            "list_scheduler": item
            }
        )
