from . import *
from .utils import People


class PessoaFisica(People):
    cpf: str
    rg: str
    pis: str
    ctps: str
    serie: str
    nancionalidade: str
    profissao: str
    nome_mae: str


class PessoaJuridica(People):
    cnpj: str
    responsavel: str
    tipo_empresa: str
    atividade_principal: str
    inscricao_municipal: str
    inscricao_estadual: str
