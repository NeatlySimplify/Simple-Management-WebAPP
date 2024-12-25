from http import HTTPStatus
from fastapi import APIRouter, Depends, Request
from .util.database import get_edgedb_client
from .util.auth import get_current_user
from .util.variables import templates


router = APIRouter(prefix='/transactions')

@router.get('/', name='get_all_action')
async def action(
    request: Request,
    session =  Depends(get_current_user),
    db_action = Depends(get_edgedb_client)
):  
    from .queries import getAllClients_async_edgeql
    from typing import List
    id = str(session)
    action_list: List[getAllClients_async_edgeql.getAllClientsResult] = getAllClients_async_edgeql.getAllClients(
        executor=db_action,
        user_id=id
        )
    return templates.TemplateResponse(
        request=request,
        name='actions.html',
        context={
            'action': action_list
        },
        status_code=HTTPStatus.OK
    )


@router.get('/income', name='income')
async def client(
    request: Request,
    session =  Depends(get_current_user),
    db_client = Depends(get_edgedb_client)
):  
    from .queries import getAllClients_async_edgeql
    from typing import List
    id = str(session)
    client_list: List[getAllClients_async_edgeql.getAllClientsResult] = getAllClients_async_edgeql.getAllClients(
        executor=db_client,
        user_id=id
        )
    return templates.TemplateResponse(
        request=request,
        name='clients.html',
        context={
            'client': client_list
        },
        status_code=HTTPStatus.OK
    )


@router.get('/expense', name='expense')
async def client(
    request: Request,
    session =  Depends(get_current_user),
    db_client = Depends(get_edgedb_client)
):  
    from .queries import getAllClients_async_edgeql
    from typing import List
    id = str(session)
    client_list: List[getAllClients_async_edgeql.getAllClientsResult] = getAllClients_async_edgeql.getAllClients(
        executor=db_client,
        user_id=id
        )
    return templates.TemplateResponse(
        request=request,
        name='clients.html',
        context={
            'client': client_list
        },
        status_code=HTTPStatus.OK
    )


@router.get('/action/form')
async def action(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.post('/action/form')
async def action(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.get('/action/{id}')
async def action(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.put('/action/{id}')
async def action(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.delete('/action/{id}')
async def action(request: Request,
                session =  Depends(get_current_user)
):
    pass