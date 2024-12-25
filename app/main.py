from fastapi import Depends, FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.queries.getBalance_async_edgeql import getBalanceResult
from .util.variables import cors_config, templates
from .util.auth import CookieInitializationMiddleware, get_current_user
from .util.database import lifetime
from .login import router as LoginRouter
from .register import router as RegisterRouter
from .transactions import router as TransactionRouter
from .client import router as ClientRouter
from .schedule import router as ScheduleRouter
from .service import router as ServiceRouter
from .user import router as UserRouter
from datetime import date

app = FastAPI(lifespan=lifetime)

app.mount("/img", StaticFiles(directory=f"./app/static/img"), name="img")
app.add_middleware(CORSMiddleware, **cors_config)
app.add_middleware(CookieInitializationMiddleware)
app.include_router(LoginRouter)
app.include_router(RegisterRouter)
app.include_router(TransactionRouter)
app.include_router(ClientRouter)
app.include_router(ScheduleRouter)
app.include_router(ServiceRouter)
app.include_router(UserRouter)


@app.get("/")
async def getDashBoard(
    request: Request,
    session: str = Depends(get_current_user),
    date = date.today()):
    from .Service.root import (
        number_of_clients,
        number_of_active_services,
        sum_of_balance_all_accounts,
        sum_of_transactions_for_month
    )
    from .queries.getTransactionsSumary_async_edgeql import getTransactionsSumaryResult
    from .queries.getBalance_async_edgeql import getBalanceResult
    balance: getBalanceResult = sum_of_balance_all_accounts(request, session)
    client_card = {
        'Clientes': number_of_clients(request, session),
        'Serviços': number_of_active_services(request, session),
        'Saldo': balance
    }
    transactions: getTransactionsSumaryResult = sum_of_transactions_for_month(
        request,
        session,
        date)
    transactions_card = {
        'Entrada': {
            'Entrada Consolidada': transactions.effective_income,
            'Entrada Prevista': transactions.total_income,
        },
        'Saída': {
            'Saída Consolidada': transactions.effective_expense,
            'Saída Prevista': transactions.total_expense ,
        },
        'Saldo do Mês': {
            'Saldo Consolidado': (transactions.effective_income - transactions.effective_expense),
            'Saldo Previsto': (transactions.total_income - transactions.total_expense) ,
        }
    }
    return templates.TemplateResponse(
        request=request,
        name='dashboard.html',
        context={
            'card': client_card,
            'transactions': transactions_card
        }
    )
