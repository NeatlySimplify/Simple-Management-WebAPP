from networkx import union_all
from pydantic import EmailStr

from . import *


class Conta_Bancaria(BaseModel):
    bank_name: str
    agency: str
    account_number: str
    saldo: float
    tipo: str


class Endereco(BaseModel):
    rua: str
    numero: str
    complemento: None | str
    bairro: str
    cep: str
    cidade: str
    estado: str


class Telefone(BaseModel):
    tipo: str
    ddd: str
    numero: str
    contato: str
    details: str


# Enums
class PeopleTag(str, Enum):
    CLIENT: str = "Cliente"
    PART: str = "Part"
    ADVERSO: str = "Adverso"
    ADVOGADO: str = "Advogado"
    ADMIN: str = "Admin"
    USER: str = "User"


class FinanceEntryTag(str, Enum):
    ENTRY: str = "Entry"
    EXIT: str = "Exit"
    TRANSFER: str = "Transfer"


class ScheduleTag(str, Enum):
    FINANCE: str = "Finance"
    USER: str = "User"
    SERVICE: str = "Service"


class PagamentoTag(str, Enum):
    UNIQUE: str = "Unique"
    DIARY: str = "Diary"
    WEAKLY: str = "Weakly"
    MONTH: str = "Month"
    YEARLY: str = "Yearly"
    CUSTOM: str = "Custom"


class RelationshipTag(str, Enum):
    CASADO: str = "Casado(a)"
    SOLTEIRO: str = "Solteiro(a)"
    VIUVO: str = "Viúvo(a)"
    UNIAO: str = "Em União Estável"
    DIVORCIADO: str = "Divorciado(a)"


# End
