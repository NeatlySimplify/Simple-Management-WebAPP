from datetime import date
import json
from . import *
from pydantic import EmailStr
from app.Model.utils import Telefone, Endereco


class People(BaseModel):
    email: EmailStr
    nome: str
    sexo: str
    estado_civil: str
    details: str = ''
    tag_tipo: str
    nascimento: date
    cidade_atual: str
    estado_atual: str
    telefone: List[Telefone]
    endereco: List[Telefone]


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


class Login(BaseModel):
    email: EmailStr
    password: str
