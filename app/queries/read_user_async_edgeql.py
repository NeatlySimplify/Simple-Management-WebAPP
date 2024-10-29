# AUTOGENERATED FROM 'app/queries/read_user.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
import datetime
import edgedb
import uuid


class NoPydanticValidation:
    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type, _handler):
        # Pydantic 2.x
        from pydantic_core.core_schema import any_schema
        return any_schema()

    @classmethod
    def __get_validators__(cls):
        # Pydantic 1.x
        from pydantic.dataclasses import dataclass as pydantic_dataclass
        _ = pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class ReadUserResult(NoPydanticValidation):
    id: uuid.UUID
    email: str
    nome: str | None
    sexo: str | None
    estado_civil: str | None
    details: str | None
    nascimento: datetime.datetime | None
    salt: str | None
    password: str
    conta: list[ReadUserResultContaItem]
    telefone: list[ReadUserResultTelefoneItem]
    endereco: list[ReadUserResultEnderecoItem]


@dataclasses.dataclass
class ReadUserResultContaItem(NoPydanticValidation):
    id: uuid.UUID
    accountNumber: str | None
    agency: str | None
    bankName: str | None
    saldo: float | None
    tipo_conta: str | None


@dataclasses.dataclass
class ReadUserResultEnderecoItem(NoPydanticValidation):
    id: uuid.UUID
    bairro: str | None
    cep: str | None
    cidade: str | None
    complemento: str | None
    estado: str | None
    numero: str | None
    rua: str | None


@dataclasses.dataclass
class ReadUserResultTelefoneItem(NoPydanticValidation):
    id: uuid.UUID
    contato: str | None
    details: str | None
    numero: str | None
    tipo: str | None


async def read_user(
    executor: edgedb.AsyncIOExecutor,
    *,
    user: uuid.UUID,
) -> ReadUserResult | None:
    return await executor.query_single(
        """\
        select User {
            id,
            email,
            nome,
            sexo,
            estado_civil,
            details,
            nascimento,
            salt,
            password,
            conta: {*},
            telefone: {*},
            endereco: {*}
        } filter .id = <uuid>$user;\
        """,
        user=user,
    )
