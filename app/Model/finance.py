from . import *
from .utils import Conta_Bancaria
from .scheduler import Scheduler


class Finance(BaseModel):
    nome: str
    valor: float
    efetivada: bool
    categoria: str
    subcategoria: str
    conta: Conta_Bancaria
    evento: List[Scheduler]
