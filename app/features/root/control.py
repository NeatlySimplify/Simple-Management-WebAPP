from typing import Any
from fastapi import Depends
from ..util.database import get_edgedb_client, handle_database_errors
from ...queries.root.getNumberOfClients_async_edgeql import getNumberOfClients
from ...queries.root.getNumberOfActiveServices_async_edgeql import getNumberOfActiveServices
from ...queries.root.getBalance_async_edgeql import getBalance, getBalanceResult
from ..util.misc import date_range
from ...queries.root.getTransactionsSumary_async_edgeql import getTransactionsSumary, getTransactionsSumaryResult


async def getTransactionsforMonth(
    date: str,
    user_id: str
) -> Any:
    transactions = await sum_of_transactions_for_month(
        user_id,
        date)
    return transactions


async def getCardsNumbers(
        user_id: str
) -> dict:
    client_card = {
        'Clientes': await number_of_clients(user_id),
        'Serviços': await number_of_active_services(user_id),
        'Saldo': await sum_of_balance_all_accounts(user_id).total
    }
    return client_card

#TODO get graphics of income, expense and balance of various accounts
# When clicking on the card it expands for differents graphics
# app.get('/')
# async def getDifferentTransactionsBoard(
#     request: Request,
#     date: str,
#     user_id: str = Depends(get_current_user),
# ):
#     result = await getTransactionsforMonth(date, user_id)
#     return templates.TemplateResponse(
#         request=request,
#         name='transactionBoxModel.html',
#         context={
#             'transactions': result
#         }
#     )
#TODO get data for other months
# When clicking on the card it expands for differents graphics
# app.post('/')
# async def postDifferentTransactionsBoard(
#     date: str,
#     user_id: str = Depends(get_current_user),
# ):
#     result = await getTransactionsforMonth(date, user_id)
#     return result


@handle_database_errors
async def number_of_clients(
    user_id: str,
    db = Depends(get_edgedb_client)
) -> int:
    result: int = getNumberOfClients(executor=db, user_id=user_id)
    return result

@handle_database_errors
async def number_of_active_services(
        user_id: str,
        db = Depends(get_edgedb_client)
) -> int:
    result: int = getNumberOfActiveServices(
        executor=db,
        user_id=user_id
    )
    return result

@handle_database_errors
async def sum_of_balance_all_accounts(
        user_id: str,
        db = Depends(get_edgedb_client)
) -> getBalanceResult:
    response = getBalance(
        executor=db,
        user_id=user_id
    )
    return response

@handle_database_errors
async def sum_of_transactions_for_month(
        user_id: str,
        date: str,
        db = Depends(get_edgedb_client)
) -> getTransactionsSumaryResult:
    dates = date_range(date)
    result = getTransactionsSumary(
        executor=db,
        user_id=user_id,
        first_day=dates.get('first'),
        last_day=dates.get('last')
    )
    return result