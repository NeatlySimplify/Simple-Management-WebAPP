# AUTOGENERATED FROM 'app/queries/getTransactionsSumary.edgeql' WITH:
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
class getTransactionsSumaryResult(NoPydanticValidation):
    id: uuid.UUID
    total_income: float
    effective_income: float
    total_expense: float
    effective_expense: float


async def getTransactionsSumary(
    executor: edgedb.AsyncIOExecutor,
    *,
    user_id: uuid.UUID,
    first_day: str,
    last_day: str,
) -> getTransactionsSumaryResult:
    return await executor.query_single(
        """\
        with user_id := (<User><uuid>$user_id),
        first_day := (cal::to_local_date(<str>$first_day)),
        last_day := (cal::to_local_date(<str>$last_day)),
        incomes := (
            select Payment {
                value,
                status
            }
            filter .user = user_id and .action.category = 'income' and ((.isDue >= first_day and .isDue < last_day) or (.paymentDate >= first_day and .paymentDate < last_day))
        ),
        expenses := (
            select Payment {
                value,
                status
            }
            filter .user = user_id and .action.category = 'expense' and ((.isDue >= first_day and .isDue < last_day) or (.paymentDate >= first_day and .paymentDate < last_day))
        )
        select {
            total_income := sum(incomes.value),
            effective_income := sum(incomes.value filter incomes.status = true),
            total_expense := sum(expenses.value),
            effective_expense := sum(expenses.value filter expenses.status = true),
        };\
        """,
        user_id=user_id,
        first_day=first_day,
        last_day=last_day,
    )
