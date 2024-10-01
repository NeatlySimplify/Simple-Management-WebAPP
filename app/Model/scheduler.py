from . import *
from datetime import datetime


class Scheduler(BaseModel):
    nome: str
    efetivado: bool
    inicio: datetime
    fim: datetime
    details: str
