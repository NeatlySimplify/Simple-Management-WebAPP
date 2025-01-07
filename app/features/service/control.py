from ..util.database import (
    get_edgedb_client,
    handle_database_errors
)
from ...queries.service import *

@handle_database_errors
async def get_sumary(
    request: Request,
    user_id: str,
    db_client = Depends(get_edgedb_client)
) -> List[getAllUnitsResult] | None:

    response = await getAllService(
        executor=db_client,
        user_id=user_id
    )
    return response
