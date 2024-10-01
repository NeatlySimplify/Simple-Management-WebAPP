from . import *
from .scheduler import Scheduler


class Service(BaseModel):
    status: str
    valor: float
    descricao: str
    events: Optional[List[Scheduler]] = []


class Process(Service):
    fase: str
    classe: str
    tipo: str
    rito: str
    forum: str
    comarca: str
    vara: str
    details: str