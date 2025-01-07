from http import HTTPStatus
from fastapi import APIRouter, Depends, Request
from ..util.database import get_edgedb_client
from ..util.auth import get_current_user
from ...main import templates
from .control import *


router = APIRouter(prefix='/schedule')

@router.get('/', name='schedule')
async def schedule(
    request: Request,
    session =  Depends(get_current_user),
    db_schedule = Depends(get_edgedb_client)
):  
    from .queries import getAllClients_async_edgeql
    from typing import List
    id = str(session)
    schedule_list: List[getAllClients_async_edgeql.getAllClientsResult] = getAllClients_async_edgeql.getAllClients(
        executor=db_schedule,
        user_id=id
        )
    schedule_active = [x for x in schedule_list if x.status]
    schedule_inactive = [x for x in schedule_list if not x.status]
    return templates.TemplateResponse(
        request=request,
        name='schedules.html',
        context={
            'schedule_active': schedule_active,
            'schedule_inactive': schedule_inactive
        },
        status_code=HTTPStatus.OK
    )


@router.get('/user', name='from_user')
async def schedule(
    request: Request,
    session =  Depends(get_current_user),
    db_schedule = Depends(get_edgedb_client)
):  
    from .queries import getAllClients_async_edgeql
    from typing import List
    id = str(session)
    schedule_list: List[getAllClients_async_edgeql.getAllClientsResult] = getAllClients_async_edgeql.getAllClients(
        executor=db_schedule,
        user_id=id
        )
    return templates.TemplateResponse(
        request=request,
        name='schedules.html',
        context={
            'schedule': schedule_list
        },
        status_code=HTTPStatus.OK
    )


@router.get('/action', name='from_action')
async def schedule(
    request: Request,
    session =  Depends(get_current_user),
    db_schedule = Depends(get_edgedb_client)
):  
    from .queries import getAllClients_async_edgeql
    from typing import List
    id = str(session)
    schedule_list: List[getAllClients_async_edgeql.getAllClientsResult] = getAllClients_async_edgeql.getAllClients(
        executor=db_schedule,
        user_id=id
        )
    return templates.TemplateResponse(
        request=request,
        name='schedules.html',
        context={
            'schedule': schedule_list
        },
        status_code=HTTPStatus.OK
    )


@router.get('/service', name='from_service')
async def schedule(
    request: Request,
    session =  Depends(get_current_user),
    db_schedule = Depends(get_edgedb_client)
):  
    from .queries import getAllClients_async_edgeql
    from typing import List
    id = str(session)
    schedule_list: List[getAllClients_async_edgeql.getAllClientsResult] = getAllClients_async_edgeql.getAllClients(
        executor=db_schedule,
        user_id=id
        )
    return templates.TemplateResponse(
        request=request,
        name='schedules.html',
        context={
            'schedule': schedule_list
        },
        status_code=HTTPStatus.OK
    )


@router.get('/schedule/form')
async def schedule(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.post('/schedule/form')
async def schedule(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.get('/schedule/{id}')
async def schedule(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.put('/schedule/{id}')
async def schedule(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.delete('/schedule/{id}')
async def schedule(request: Request,
                session =  Depends(get_current_user)
):
    pass