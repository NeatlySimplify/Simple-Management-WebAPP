from fastapi import APIRouter, Depends, Request

from .util.database import get_edgedb_client
from .util.auth import get_current_user
from .util.variables import templates


router = APIRouter(prefix='/client')

@router.get('/')
async def client(
    request: Request,
    session =  Depends(get_current_user),
    db_client = Depends(get_edgedb_client)
):  
    from .queries.
    from .util.variables import templates
    return


@router.get('/client/form')
async def client(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.post('/client/form')
async def client(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.get('/client/{id}')
async def client(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.put('/client/{id}')
async def client(request: Request,
                session =  Depends(get_current_user)
):
    pass


@router.delete('/client/{id}')
async def client(request: Request,
                session =  Depends(get_current_user)
):
    pass