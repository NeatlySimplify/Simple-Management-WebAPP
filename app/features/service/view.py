from http import HTTPStatus
from fastapi import APIRouter, Depends, Request
from ..util.auth import get_current_user
from ...util import templates
from .control import (
    get_sumary
)

router = APIRouter(prefix='/service')

@router.get('/', name='getAllServices')
async def getSumary(
    request: Request,
    session =  Depends(get_current_user),
):
    result = await get_sumary(request, str(session))
    return templates.TemplateResponse(
        request=request,
        name='services.html',
        context={
            'service': result
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
