from fastapi import APIRouter, Request, HTTPException
from http import HTTPStatus
from .Model.register import Register


router = APIRouter(prefix="/register")

@router.get('/')
async def register(request: Request):
    from .util.variables import templates
    from .util.auth import verify, decode_token
    token = request.cookies.get("access_token")
    try:
        decoded = decode_token(token)  
        authenticated = verify(decoded)
        if authenticated:
            raise HTTPException(
                        status_code=HTTPStatus.TEMPORARY_REDIRECT,
                        detail="Authenticated",
                        headers={"Location": "/"}
                    )
    except:
        pass
    return templates.TemplateResponse(
        request=request,
        name='pre_access_registration.html',
        status_code=200
    )

@router.post('/')
async def register(
    request: Request,
    data: Register,
):
    from .util.auth import hash_password
    from .Service.preAccess import register
    hashed_password = hash_password(data.password)
    try:
        return await register(request, data, hashed_password)
    except HTTPException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail={
                "status": "error",
                "message": e.detail
            }
        )