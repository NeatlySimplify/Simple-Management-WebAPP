from enum import Enum
from pydantic import BaseModel, EmailStr, Json
from typing import Optional, List
from datetime import date


class ClientsType(str, Enum):
    PF: str = "Pessoa Física"
    PJ: str = "Pessoa Jurídica"


class RelationshipTag(str, Enum):
    CASADO: str = "Casado(a)"
    SOLTEIRO: str = "Solteiro(a)"
    VIUVO: str = "Viúvo(a)"
    UNIAO: str = "Em União Estável"
    DIVORCIADO: str = "Divorciado(a)"


class SexTag(str, Enum):
    HOMEM: str = 'Homem'
    MULHER: str = 'Mulher'


class Endereco(BaseModel):
    rua: str = ''
    numero: str = ''
    complemento: str = ''
    bairro: str = ''
    cep: str = ''
    cidade: str = ''
    estado: str = ''


class Telefone(BaseModel):
    ddd: str = ''
    numero: str = ''
    contato: str = ''
    details: str = ''


class Client(BaseModel):
    email: EmailStr
    name: str
    sex: SexTag
    template_model: Optional[str] = None
    relationship: RelationshipTag
    govt_id: str
    details: Optional[str] = None
    type_client: ClientsType
    birth: date
    custom_fields: Optional[Json] = None
    phone: Optional[List[Telefone]] = None
    address: Optional[List[Endereco]] = None


# class PessoaFisica(BaseModel):
#     user: str
#     cpf: str
#     rg: str
#     pis: str
#     ctps: str
#     serie: str
#     nancionalidade: str
#     profissao: str
#     nome_mae: str


# class PessoaJuridica(BaseModel):
#     user: str
#     cnpj: str
#     responsavel: str
#     tipo_empresa: str
#     atividade_principal: str
#     inscricao_municipal: str
#     inscricao_estadual: str
