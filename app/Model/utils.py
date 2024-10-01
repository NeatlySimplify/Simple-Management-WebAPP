from . import *
from pydantic import EmailStr
from .scheduler import Scheduler


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


# Template para outras classes.
class People(BaseModel):
    nome: str
    evento: List[Scheduler]
    sexo: str
    estado_civil: str
    telefone: List[Telefone]
    endereco: List[Endereco]
    email: EmailStr
    details: str = ''
    tagPessoa: str

# Enums
class TipoPessoa(str, Enum):
    CLIENT: str = "Cliente"
    PART: str = "Part"
    ADVERSO: str = "Adverso"
    ADVOGADO: str = "Advogado"
    ADMIN: str = "Admin"


class FinanceEntryType(str, Enum):
    ENTRY: str = "Entry"
    EXIT: str = "Exit"
    TRANSFER: str = "Transfer"


class ScheduleTag(str, Enum):
    FINANCE: str = "Finance"
    USER: str = "User"
    SERVICE: str = "Service"
    CLIENT: str = "Client"

# End