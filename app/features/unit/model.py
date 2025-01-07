from enum import Enum
from pydantic import BaseModel, EmailStr, Json
from typing import Optional, List
from datetime import date


class ClientsType(str, Enum):
    PF: str = "PF"
    PJ: str = "PJ"

    def display(self) -> str:
        return {
            self.PF: "Pessoa Física",
            self.PJ: "Pessoa Jurídica"
        }[self]


class RelationshipTag(str, Enum):
    CASADO: str = "CASADO"
    SOLTEIRO: str = "SOLTEIRO"
    VIUVO: str = "VIUVO"
    UNIAO: str = "UNIAO"
    DIVORCIADO: str = "DIVORCIADO"

    def display(self) -> str:
        return {
            self.CASADO: "Casado(a)",
            self.SOLTEIRO: "Solteiro(a)",
            self.VIUVO: "Viúvo(a)",
            self.UNIAO: "Em União Estável",
            self.DIVORCIADO: "Divorciado(a)"
        }[self]


class SexTag(str, Enum):
    HOMEM: str = 'HOMEM'
    MULHER: str = 'MULHER'

    def display(self) -> str:
        return {
            self.HOMEM: 'Homem',
            self.MULHER: 'Mulher'
        }[self]


class Address(BaseModel):
    street: str
    number: str
    complement: Optional[str] = None
    district: str
    postal: Optional[str] = None
    city: str
    state: str


class Contact(BaseModel):
    number: str
    contact: Optional[str] = None
    complement: Optional[str] = None


class Unit(BaseModel):
    email: EmailStr
    name: str
    sex: SexTag
    template_model: Optional[str] = None
    relationship: RelationshipTag
    type_client: ClientsType
    govt_id: str
    birth: date
    details: Optional[str] = None
    phone: Optional[Contact] = None
    address: Optional[Address] = None
    custom_fields: Optional[Json] = None

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
