from http import HTTPStatus
from fastapi import APIRouter, Depends, Request
from .util.auth import get_current_user
from .util.variables import templates
from .Model.clients import Client


router = APIRouter(prefix='/client')

@router.get('/', name='get_all_clients')
async def get_sumary(
    request: Request,
    session =  Depends(get_current_user),
):  
    from .Service.client import get_sumary

    id = str(session)
    result = get_sumary(request, id)
    """ return templates.TemplateResponse(
        request=request,
        name='clients.html',
        context={
            'client': result
        },
        status_code=HTTPStatus.OK
    ) """
    return HTTPStatus.OK

@router.get('/form', name='getClientForm')
async def get_one(request: Request,
    session =  Depends(get_current_user)
):
    """ return templates.TemplateResponse(
        request,
        'clientForm.html'
    ) """
    return HTTPStatus.OK

@router.get('/form', name='getCustomClientForm')
async def client(request: Request,
                custom: str,
                session =  Depends(get_current_user)
):
    #from .queries.getTemplate_async_edgeql import getTemplate, getTemplateResult
    #from .Service.user import get_template
    
    # user_id = str(session)
    # result = get_template(user_id, custom)
    """ return templates.TemplateResponse(
        request,
        'clientForm.html',
        context={
            #'customFields': result
        }
    ) """
    return HTTPStatus.OK

@router.get('/{id}', name='get_client_with_id')
async def client(
    request: Request,
    id: str,
    session =  Depends(get_current_user)
):
    from .Service.client import get_one

    result = get_one(request, id, str(session))
    """ return templates.TemplateResponse(
        request,
        'clientModel.html',
        context={
            'client': result
        }
    ) """
    return HTTPStatus.OK

@router.put('/{id}', name='put_client_with_id')
async def client(
    request: Request,
    id: str,
    client: Client,
    session =  Depends(get_current_user)
):
    from .Service.client import update

    result = update(request, client, id, str(session))
    # return result 
    return HTTPStatus.ACCEPTED

@router.delete('/{id}', name='delete_client_with_id')
async def client(
    request: Request,
    id: str,
    session =  Depends(get_current_user)
):
    from .Service.client import delete

    result = delete(request, id)
    # return result
    return HTTPStatus.ACCEPTED
