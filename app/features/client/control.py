from ..util.database import get_edgedb_client, handle_database_errors
from fastapi import Request, Depends
from ..Model.clients import Client


@handle_database_errors
async def get_sumary(
    request: Request,
    user_id: str,
    db_client = Depends(get_edgedb_client)
):
    from ..queries.getAllClients_async_edgeql import getAllClients, getAllClientsResult
    from typing import List
    response: List[getAllClientsResult] = getAllClients(
        executor=db_client,
        user_id=user_id
    )
    return response

@handle_database_errors
async def get_one(
    request: Request,
    client_id: str,
    db = Depends(get_edgedb_client)
):
    from ..queries.getClient_async_edgeql import getClient, getClientResult

    result: getClientResult = getClient(
        executor=db,
        id=client_id
    )
    return result

@handle_database_errors
async def create(
    client: Client,
    user_id: str,
    db_client = Depends(get_edgedb_client)
):
    from ..queries.createClient_async_edgeql import createClient, createClientResult

    result: createClientResult = createClient(
        executor=db_client,
        user_id=user_id,
        email=client.email,
        name=client.name,
        template_model=client.template_model,
        relationship=client.relationship,
        govt_id=client.govt_id,
        sex=client.sex,
        details=client.details,
        type_client=client.type_client,
        birth=client.birth,
        custom_fields=client.custom_fields,
    )
    return result

@handle_database_errors
async def update(
    request: Request,
    client: Client,
    id: str,
    db_client = Depends(get_edgedb_client)
):
    from ..queries.updateClient_async_edgeql import updateClient, updateClientResult

    result: updateClientResult = updateClient(
        id=id,
        executor=db_client,
        email=client.email,
        name=client.name,
        relationship=client.relationship,
        govt_id=client.govt_id,
        sex=client.sex,
        details=client.details,
        type_client=client.type_client,
        birth=client.birth,
        custom_fields=client.custom_fields,
    )
    return result

@handle_database_errors
async def delete(
    request: Request,
    client_id: str,
    db = Depends(get_edgedb_client)
):
    from ..queries.deleteClient_async_edgeql import deleteClient, deleteClientResult

    result: deleteClientResult = deleteClient(
        executor=db,
        id=client_id
    )
    return result