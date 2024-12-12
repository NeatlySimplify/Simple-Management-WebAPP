import edgedb
from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import JSONResponse
from http import HTTPStatus
from edgedb import errors
from .util.database import get_edgedb_client
from .Model.register import Register


router = APIRouter(prefix="/register")


@router.get('/')
async def register(request: Request):
    from .util.variables import templates
    from .util.auth import verify, decode_token
    token = request.cookies.get("access_token")
    try:
        print(token)
        decoded = decode_token(token)  
        print(decoded)
        authenticated = verify(decoded)
        print(authenticated)
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
    data: Register,
    db: edgedb.AsyncIOClient = Depends(get_edgedb_client)
):
    from app.queries.create_user_async_edgeql import create_user
    from .util.auth import hash_password
    hashed_password = hash_password(data.password)
    try:
        await create_user(
        executor=db,
        email=data.email,
        name=data.name,
        password=hashed_password,
        )
        return JSONResponse(
            status_code=HTTPStatus.CREATED,
            content={
                'status': 'success',
                'message': 'User created Successfully.'
            }
        )
    
    except errors.ConstraintViolationError:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={
                "status": "error",
                "message": "User already exists"
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={
                "status": "error",
                "message": "An unexpected error occurred.",
                "details": str(e)
            }
        )