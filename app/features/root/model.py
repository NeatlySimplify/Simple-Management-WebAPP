from pydantic import BaseModel, model_validator


class TransactionsForMonth(BaseModel):
    total_income: float
    expected_income: float
    total_exit: float
    expected_exit: float
    balance: float = total_income - total_exit
    expected_balance : float = expected_income - expected_exit