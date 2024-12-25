from fastapi import APIRouter, HTTPException, Request
from http import HTTPStatus
from .Model.preAccess import Login

router = APIRouter(prefix='/login')

@router.get('/')
async def login(request: Request):
    from .main import templates
    from .util.auth import verify, decode_token
    token = request.cookies.get("access_token")
    try:    
        authenticated = verify(decode_token(token))
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
        name='pre_access_login.html',
        status_code=200
    )

@router.post("/")
async def login(
    request: Request,
    data: Login,
):
    from .Service.preAccess import login
    from .util.auth import tokens, create_access_token
    from .util.auth import verify_password
    try:
        result = await login(request, data)
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
            tokens[access_token] = {"sub": result.id, 'password': result.password}
            return {
                'content':{
                    'status': 'success',
                    "message": "Welcome"
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
