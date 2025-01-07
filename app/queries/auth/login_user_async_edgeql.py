# AUTOGENERATED FROM 'app/queries/auth/login_user.edgeql' WITH:
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
class LoginUserResult(NoPydanticValidation):
    id: uuid.UUID
    name: str
    password: str
    account: list[LoginUserResultAccountItem]


@dataclasses.dataclass
class LoginUserResultAccountItem(NoPydanticValidation):
    id: uuid.UUID
    balance: float | None
    accountNumber: str | None
    accountType: str | None
    agency: str | None
    bankName: str | None


async def login_user(
    executor: edgedb.AsyncIOExecutor,
    *,
    email: str,
) -> LoginUserResult | None:
    return await executor.query_single(
        """\
        select (
            update User filter .email = <str>$email set {
                isActive := <bool>true,
                lastActiveDate := datetime_of_statement()
            }
        ) {
            id,
            name,
            password,
            account: {*}
        } limit 1;\
        """,
        email=email,
    )
