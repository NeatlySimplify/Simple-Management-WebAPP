from ..util.database import get_edgedb_client, handle_database_errors
from fastapi import Request, Depends
from .model import Unit, Address, Contact
from ...queries.unit import *
from typing import List

@handle_database_errors
async def get_sumary(
    request: Request,
    user_id: str,
    db_client = Depends(get_edgedb_client)
) -> List[getAllUnitsResult] | None:
    
    response = await getAllUnits(
        executor=db_client,
        user_id=user_id
    )
    return response

@handle_database_errors
async def get_one(
    request: Request,
    unit_id: str,
    db = Depends(get_edgedb_client)
) -> getUnitResult | None:
    result = await getUnit(
        executor=db,
        id=unit_id
    )
    return result

@handle_database_errors
async def get_sumary_of_template(
    request: Request,
    user_id: str,
    template_name,
    db_client = Depends(get_edgedb_client)
) -> List[getAllUnitsFromTemplateResult] | None:
    
    return await getAllUnitsFromTemplate(
        executor=db_client,
        user_id=user_id,
        template_name=template_name
    )

@handle_database_errors
async def create_unit(
    request: Request,
    unit: Unit,
    user_id: str,
    db_client = Depends(get_edgedb_client)
):
    return await createUnit(
        executor=db_client,
        user_id=user_id,
        email=unit.email,
        name=unit.name,
        template_model=unit.template_model,
        relationship=unit.relationship,
        govt_id=unit.govt_id,
        sex=unit.sex,
        details=unit.details,
        type_unit=unit.type_unit,
        birth=unit.birth,
        custom_fields=unit.custom_fields,
        phoneComplement=unit.phone.complement,
        phoneNumber=unit.phone.number,
        contact=unit.phone.contact,
        state=unit.address.state,
        city=unit.address.city,
        district=unit.address.district,
        street=unit.address.street,
        addressNumber=unit.address.number,
        addressComplement=unit.address.complement,
        postal=unit.address.postal
    )

@handle_database_errors
async def update_unit(
    request: Request,
    unit: Unit,
    id: str,
    db_client = Depends(get_edgedb_client)
):
    return await updateUnit(
        id=id,
        executor=db_unit,
        email=unit.email,
        name=unit.name,
        relationship=unit.relationship,
        govt_id=unit.govt_id,
        sex=unit.sex,
        details=unit.details,
        type_unit=unit.type_unit,
        birth=unit.birth,
        custom_fields=unit.custom_fields,
    )

@handle_database_errors
async def update_address(
    address: Address,
    address_id: str,
    db_client = Depends(get_edgedb_client)
):
    return await updateAddress(
        executor=db_client,
        address_id=address_id,
        state=address.state,
        city=address.city,
        district=address.district,
        street=address.street,
        number=address.number,
        complement=address.complement,
        postal=address.postal
    )

@handle_database_errors
async def update_phone(
    phone: Contact,
    phone_id: str,
    db_client = Depends(get_edgedb_client)
):
    return await updatePhone(
        executor=db_client,
        phone_id=phone_id,
        number=phone.number,
        contact=phone.contact,
        complement=phone.complement
    )

@handle_database_errors
async def delete_unit(
    request: Request,
    unit_id: str,
    db = Depends(get_edgedb_client)
):
    return await deleteUnit(
        executor=db,
        id=unit_id
    )

@handle_database_errors
async def delete_address(
    request: Request,
    address_id: str,
    db = Depends(get_edgedb_client)):
    return await deleteAddress(
        executor=db,
        address_id=address_id
    )

@handle_database_errors
async def delete_phone(
    request: Request,
    phone_id: str,
    db = Depends(get_edgedb_client)
):
    return await deletePhone(
        executor=db,
        phone_id=phone_id
    )
