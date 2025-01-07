from http import HTTPStatus
from typing import Optional
from fastapi import APIRouter, Depends, Request
from ..util.auth import get_current_user
from ...util import templates
from .model import Unit
from http import HTTPStatus
from .control import (
    get_sumary,
    get_sumary_of_template,
    get_one,
    create_client,
    update_address,
    update_client,
    update_phone,
    delete_address,
    delete_client,
    delete_phone
)

router = APIRouter(prefix='/client')

stateList = [
    ['AC', 'Acre'],
    ['AL', 'Alagoas'],
    ['AP', 'Amapá'],
    ['AM', 'Amazonas'],
    ['BA', 'Bahia'],
    ['DF', 'Distrito Federal'],
    ['ES', 'Espírito Santo'],
    ['GO', 'Goiás'],
    ['MA', 'Maranhão'],
    ['MT', 'Mato Grosso'],
    ['MS', 'Mato Grosso do Sul'],
    ['MG', 'Minas Gerais'],
    ['PA', 'Pará'],
    ['PB', 'Paraíba'],
    ['PR', 'Paraná'],
    ['PE', 'Pernambuco'],
    ['PI', 'Piauí'],
    ['RJ', 'Rio de Janeiro'],
    ['RN', 'Rio Grande do Norte'],
    ['RS', 'Rio Grande do Sul'],
    ['RO', 'Rondônia'],
    ['RR', 'Roraima'],
    ['SC', 'Santa Catarina'],
    ['SP', 'São Paulo'],
    ['SE', 'Sergipe'],
    ['TO', 'Tocantins']
]

## GET ##
@router.get('/', name='getAllUnits')
async def getSumary(
    request: Request,
    session =  Depends(get_current_user),
):
    result = await get_sumary(request, str(session))
    return templates.TemplateResponse(
        request=request,
        name='unit.html',
        context={
            'unit': result
        },
        status_code=HTTPStatus.OK
    )

@router.get('/form', name='getUnitForm')
async def getForm(
    request: Request,
    id: Optional[str],
    session =  Depends(get_current_user)
):
    result = None
    if id is not None:
        result = await get_one(request, id)
    return templates.TemplateResponse(
        request,
        'forms/client.html',
        context={
            'stateList': stateList,
            'data': result
        },
        status_code=HTTPStatus.OK
    )

@router.get('/{client_id}', name='getUnit')
async def getUnit(
    request: Request,
    id: str,
    session =  Depends(get_current_user)
):
    result = await get_one(request, id)
    return templates.TemplateResponse(
        request,
        'clientModel.html',
        context={
            'client': result
        }
    )
## GET END

## POST
@router.post('/', name='createUnit')
async def addUnit(
    request: Request,
    data: Unit,
    session =  Depends(get_current_user)
):
    await create_client(request, data, str(session))
    return HTTPStatus.ACCEPTED
## POST END

## PUT
@router.put('/{id}', name='updateUnit')
async def updateUnit(
    request: Request,
    id: str,
    client: Unit,
    session =  Depends(get_current_user)
):
    await update_client(request, client, id)
    # return result
    return HTTPStatus.ACCEPTED
## PUT END

## DELETE
@router.delete('/{id}', name='deleteUnit')
async def deleteUnit(
    request: Request,
    id: str,
    session =  Depends(get_current_user)
):
    await delete_client(request, id)
    # return result
    return HTTPStatus.ACCEPTED
## DELETE END

## TODO other Routes

""" @router.get('/{template_name}', name='getAllUnitsFilterTemplate')
async def getSumaryFromTemplates(
    request: Request,
    template_name: str,
    session =  Depends(get_current_user),
):
    result = await get_sumary_of_template(request, str(session), template_name)
    return templates.TemplateResponse(
        request=request,
        name='clients.html',
        context={
            'client': result
        },
        status_code=HTTPStatus.OK
    )

@router.get('/form', name='getCustomClientForm')
async def getCustomForm(request: Request,
                custom: str,
                session =  Depends(get_current_user)
):
    # user_id = str(session)
    # result = get_template(user_id, custom)
    return templates.TemplateResponse(
        request,
        'clientCustomForm.html',
        context={
            #'customFields': result
        }
    )
    return HTTPStatus.OK

@router.get('/phoneform', name='getPhoneForm')
async def getPhoneForm(
    request: Request,
    client_id: str,
    session =  Depends(get_current_user)
):
    return templates.TemplateResponse(
        request,
        'phoneForm.html'
    )

@router.get('/addressform', name='getAddressForm')
async def getAddressForm(
    request: Request,
    client_id: str,
    session =  Depends(get_current_user)
):
    return templates.TemplateResponse(
        request,
        'addressForm.html'
    )

@router.put('/address/{id}', name='updateAddress')
async def updateAddress(
    request: Request,
    id: str,
    address: Address,
    session =  Depends(get_current_user)
):
    result = await update_address(request, address, id)
    # return result
    return HTTPStatus.ACCEPTED

@router.put('/phone/{id}', name='updatePhone')
async def updatePhone(
    request: Request,
    id: str,
    phone: Contact,
    session =  Depends(get_current_user)
):
    result = await update_phone(request, phone, id)
    # return result
    return HTTPStatus.ACCEPTED

@router.delete('/address/{id}', name='deleteAddress')
async def deleteAddress(
    request: Request,
    id: str,
    session =  Depends(get_current_user)
):
    result = await delete_address(request, id)
    # return result
    return HTTPStatus.ACCEPTED

@router.delete('/phone/{id}', name='deletePhone')
async def deletePhone(
    request: Request,
    id: str,
    session =  Depends(get_current_user)
):
    result = await delete_phone(request, id)
    # return result
    return HTTPStatus.ACCEPTED
"""
