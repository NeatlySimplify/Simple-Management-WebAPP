from fastapi import APIRouter, Depends, HTTPException, Request
from http import HTTPStatus
from .model import Login
from ...main import templates
from .control import login as C_login
from ..util.auth import create_access_token
from ..util.password import verify_password
from .dependency import redirect_if_authenticated


router = APIRouter(prefix='/login')

@router.get('/')
async def login(
    request: Request,
    redirect=Depends(redirect_if_authenticated)
):
    return templates.TemplateResponse(
        request=request,
        name='pre_access_login.html',
        status_code=HTTPStatus.OK
    )

@router.post("/")
async def login(
    data: Login,
):
    try:
        result = await C_login(data)
        validate = verify_password(data.password, result.password)
        if not validate:
            return {
                'content':{
                    'status': 'error',
                    "message": "Wrong Password"
                }, 
                'status_code': HTTPStatus.UNAUTHORIZED
            }
        else:
            access_token = create_access_token(str(result.id))
            return {
                'content':{
                    'status': 'success',
                    "message": "Welcome",
                    'token': access_token
                }, 
                'status_code': HTTPStatus.OK
            }
    except HTTPException as e:
        raise HTTPException(
            status_code=e.status_code,
            content={
                "status": "error",
                "message": e.detail
            }
        )
