# AUTOGENERATED FROM 'app/queries/user/logout.edgeql' WITH:
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
class LogoutResult(NoPydanticValidation):
    id: uuid.UUID


async def logout(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
) -> LogoutResult | None:
    return await executor.query_single(
        """\
        update User filter .id = <uuid>$id set {
            isActive := <bool>false
        }\
        """,
        id=id,
    )
