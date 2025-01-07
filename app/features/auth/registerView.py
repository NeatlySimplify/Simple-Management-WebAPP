from fastapi import APIRouter, Depends, Request, HTTPException
from http import HTTPStatus
from .model import Register
from ...main import templates
from .control import register as C_register
from .dependency import redirect_if_authenticated


router = APIRouter(prefix="/register")

@router.get('/')
def register(
    request: Request, 
    redirect=Depends(redirect_if_authenticated)
):
    return templates.TemplateResponse(
        request=request,
        name='pre_access_registration.html',
        status_code=HTTPStatus.OK
    )

@router.post('/')
async def register(
    data: Register,
):
    try:
        return await C_register(data)
    except HTTPException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail={
                "status": "error",
                "message": e.detail
            }
        )