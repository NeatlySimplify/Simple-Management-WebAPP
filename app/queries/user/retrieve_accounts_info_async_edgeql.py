# AUTOGENERATED FROM 'app/queries/retrieve_accounts_info.edgeql' WITH:
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
class RetrieveAccountsInfoResult(NoPydanticValidation):
    id: uuid.UUID
    bankName: str | None
    accountNumber: str | None
    balance: float | None
    accountType: str | None
    sumary: list[RetrieveAccountsInfoResultSumaryItem]


@dataclasses.dataclass
class RetrieveAccountsInfoResultSumaryItem(NoPydanticValidation):
    id: uuid.UUID
    year: int | None
    month: int | None
    expense: float | None
    income: float | None


async def retrieve_accounts_info(
    executor: edgedb.AsyncIOExecutor,
    *,
    user: uuid.UUID,
) -> RetrieveAccountsInfoResult | None:
    return await executor.query_single(
        """\
        select User.account {
                bankName,
                accountNumber,
                balance,
                accountType,
                sumary: {
                        year,
                        month,
                        expense,
                        income
                }
        } filter .id = <uuid>$user;\
        """,
        user=user,
    )
