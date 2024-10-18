from . import *


class Finance(BaseModel):
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