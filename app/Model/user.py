from . import *
from .utils import People, Conta_Bancaria
from .scheduler import Scheduler


class User(People):
    role: str
    password: str
    conta: Optional[List[Conta_Bancaria]] = []
    events: Optional[List[Scheduler]] = []
