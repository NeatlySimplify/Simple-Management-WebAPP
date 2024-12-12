from fastapi import APIRouter, Depends
from http import HTTPStatus
from app.util import get_current_user


router = APIRouter(
    prefix="/user",
    dependencies=[Depends(get_current_user)],
    responses={
        HTTPStatus.NOT_FOUND: {"description": "Not found"},
        HTTPStatus.ACCEPTED: {"description": "Success"},
        HTTPStatus.BAD_REQUEST: {"description": "Bad Request"},
        HTTPStatus.CREATED: {"description": "Created with Success"},
        HTTPStatus.INTERNAL_SERVER_ERROR: {"description": "Error on Server"},
        HTTPStatus.REQUEST_TIMEOUT: {"description": "The server is late"},
    },
)


@router.get("/")
async def get_perfil():
    pass


@router.get("/templates")
async def get_templates():
    pass


@router.get("/{id}")
async def read_user(id: str):
    pass


@router.put("/{id}")
async def update_user(id: str):
    pass

@router.post("/{id}")
async def post_user(id: str):
    pass


@router.delete("/{id}")
async def delete_user(id: str):
    pass