from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class Transactions(BaseModel):
    user: str
    nome: str
    valor: float
    parcelas: int
    periodicidade: str
    efetivado: bool
    tag_tipo: str
    categoria: str
    details: str = ''
    subcategoria: str


class Pagamento(BaseModel):
    valor: float
    data_pagamento: datetime
    status: bool
    parcela: int


class FinanceEntryTag(str, Enum):
    ENTRY: str = "Entry"
    EXIT: str = "Exit"
    TRANSFER: str = "Transfer"


class PagamentoTag(str, Enum):
    UNIQUE: str = "Unique"
    DIARY: str = "Diary"
    WEAKLY: str = "Weakly"
    MONTH: str = "Month"
    YEARLY: str = "Yearly"
    CUSTOM: str = "Custom"


