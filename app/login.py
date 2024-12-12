import edgedb
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from .util.database import get_edgedb_client
from http import HTTPStatus
from .Model.login import Login

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
    response: Response,
    form_data: Login,
    db: edgedb.AsyncIOClient = Depends(get_edgedb_client)
):
    from .queries import login_user_async_edgeql
    from .util.auth import tokens, create_access_token
    from .util.auth import verify_password
    from edgedb import errors
    try:
        result: login_user_async_edgeql.LoginUserResult = await login_user_async_edgeql.login_user(
            executor=db,
            email=form_data.email
        )
        validate = verify_password(form_data.password, result.password)
    except errors.NoDataError:
            return JSONResponse(
                content={
                    "message": "This user doesn't exist, you should try registering or try another email"
                },
                status_code=HTTPStatus.NOT_FOUND)
    except errors.ClientConnectionError:
        return JSONResponse(
            content={
                "message": "This service is unavailable right now, you should try later"
            }, status_code=HTTPStatus.SERVICE_UNAVAILABLE)
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "status": "error",
                "message": e.detail
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
    if not validate:
        return JSONResponse(content={"message": "Wrong Password"}, status_code=HTTPStatus.UNAUTHORIZED)
    else:
        access_token = create_access_token(str(result.id))
        tokens[access_token] = {"sub": result.id, 'password': result.password}
        return JSONResponse(content={"message": "Welcome", 'access_token': access_token}, status_code=HTTPStatus.OK)
