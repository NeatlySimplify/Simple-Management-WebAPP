from . import *
from datetime import datetime


class Scheduler(BaseModel):
    user: str
    nome: str
    status: bool
    inicio: datetime
    fim: datetime
    details: str = ''
    tag_tipo: str
