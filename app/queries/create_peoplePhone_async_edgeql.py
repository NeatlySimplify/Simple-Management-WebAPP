# AUTOGENERATED FROM 'app/queries/create_peoplePhone.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
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
class CreatePeoplephoneResult(NoPydanticValidation):
    id: uuid.UUID


async def create_peoplePhone(
    executor: edgedb.AsyncIOExecutor,
    *,
    tipo: str,
    numero: str,
    contato: str,
    details: str,
    id: uuid.UUID,
) -> CreatePeoplephoneResult | None:
    return await executor.query_single(
        """\
        # Funciona com User, PessoaFisica e PessoaJuridica
        update People filter .id = <uuid>$id set {
            telefone += (insert Phone {
                    tipo:= <json>$tipo,
                    numero:= <str>$numero,
                    contato:= <str>$contato,
                    details:= <str>$details
                }
            )
        }\
        """,
        tipo=tipo,
        numero=numero,
        contato=contato,
        details=details,
        id=id,
    )
