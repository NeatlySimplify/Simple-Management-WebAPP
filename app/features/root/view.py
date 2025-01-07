from .control import getCardsNumbers, getTransactionsforMonth
from ..util.auth import get_current_user
from app.util import templates
from datetime import date
from fastapi import Request, Depends
from fastapi import APIRouter
#TODO get templates names for sidebar menu

root = APIRouter()

@root.get('/', name='getDashBoard')
async def getDashBoard(
    request: Request,
    user_id: str = Depends(get_current_user),
    date = date.today()):
    client_card = await getCardsNumbers(user_id)
    transactions_card = await getTransactionsforMonth(date, user_id)
    return templates.TemplateResponse(
        request=request,
        name='dashboard.html',
        context={
            'above_card': client_card,  # For dashboard
            'below_card': transactions_card,  # For dashboard
            'clientTemplates': {}, # For sidebar menu
            'serviceTemplates': {}, # For sidebar menu
            'schedulerList': {} # For the schedule table
        }
    )

