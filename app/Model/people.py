from . import *
from pydantic import EmailStr


class People(BaseModel):
    email: EmailStr
    nome: str
    sexo: str
    estado_civil: str
    details: str = ''
    tag_tipo: str


class PessoaFisica(People):
    user: str
    cpf: str
    rg: str
    pis: str
    ctps: str
    serie: str
    nancionalidade: str
    profissao: str
    nome_mae: str


class PessoaJuridica(People):
    user: str
    cnpj: str
    responsavel: str
    tipo_empresa: str
    atividade_principal: str
    inscricao_municipal: str
    inscricao_estadual: str


class User(People):
    password: str
    salt: str
