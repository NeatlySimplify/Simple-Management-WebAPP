from http import HTTPStatus
from fastapi import APIRouter, Depends, Request
from .util.database import get_edgedb_client
from .util.auth import get_current_user
from .util.variables import templates


router = APIRouter(prefix='/service')

@router.get('/', name='get_all_service')
async def service(
    request: Request,
    session =  Depends(get_current_user),
    db_service = Depends(get_edgedb_client)
):  
    from .queries import getAllClients_async_edgeql
    from typing import List
    id = str(session)
    service_list: List[getAllClients_async_edgeql.getAllClientsResult] = getAllClients_async_edgeql.getAllClients(
        executor=db_service,
        user_id=id
        )
    return templates.TemplateResponse(
        request=request,
        name='services.html',
        context={
            'service': service_list
        },
        status_code=HTTPStatus.OK
    )



@router.get('/service/form')
async def service(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.post('/service/form')
async def service(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.get('/service/{id}')
async def service(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.put('/service/{id}')
async def service(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.delete('/service/{id}')
async def service(request: Request,
                session =  Depends(get_current_user)
):
    pass