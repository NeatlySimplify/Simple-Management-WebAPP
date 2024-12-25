from fastapi import Request, Depends
from ..util.database import get_edgedb_client, handle_database_errors

@handle_database_errors
async def number_of_clients(
    request: Request,
    user_id: str,
    db = Depends(get_edgedb_client)
):
    from ..queries.getNumberOfClients_async_edgeql import getNumberOfClients
    result: int = getNumberOfClients(
        executor=db,
        user_id=user_id
    )
    return result

@handle_database_errors
async def number_of_active_services(
        request: Request,
        user_id: str,
        db = Depends(get_edgedb_client)
):
    from ..queries.getNumberOfActiveServices_async_edgeql import getNumberOfActiveServices
    result: int = getNumberOfActiveServices(
        executor=db,
        user_id=user_id
    )
    return result

@handle_database_errors
async def sum_of_balance_all_accounts(
        request: Request,
        user_id: str,
        db = Depends(get_edgedb_client)
):
    from ..queries.getBalance_async_edgeql import getBalance, getBalanceResult
    response: getBalanceResult = getBalance(
        executor=db,
        user_id=user_id
    )
    return response

@handle_database_errors
async def sum_of_transactions_for_month(
        request: Request,
        user_id: str,
        date: str,
        db = Depends(get_edgedb_client)
):
    from ..util.misc import date_range
    from ..queries.getTransactionsSumary_async_edgeql import getTransactionsSumary, getTransactionsSumaryResult
    dates = date_range(date)
    result: getTransactionsSumaryResult = getTransactionsSumary(
        executor=db,
        user_id=user_id,
        first_day=dates.get('first'),
        last_day=dates.get('last')
    )
    return result
