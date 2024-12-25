from http import HTTPStatus
from fastapi import APIRouter, Depends, Request
from .util.database import get_edgedb_client
from .util.auth import get_current_user
from .util.variables import templates


router = APIRouter(prefix='/user')

@router.get('/', name='perfil')
async def user(
    request: Request,
    session =  Depends(get_current_user),
    db_user = Depends(get_edgedb_client)
):  
    
    
    return templates.TemplateResponse(
        request=request,
        name='users.html',
        context={
            'user': user_list
        },
        status_code=HTTPStatus.OK
    )


@router.get('/templates', name='templates')
async def user(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.get('/logout', name='logout')
async def user(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.get('/user/form')
async def user(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.post('/user/form')
async def user(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.get('/user/{id}')
async def user(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.put('/user/{id}')
async def user(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.delete('/user/{id}')
async def user(request: Request,
                session =  Depends(get_current_user)
):
    pass