from uuid import UUID
from pydantic import EmailStr, BaseModel, Json, model_validator
from typing import Optional, List


class BankAccount(BaseModel):
    bankName: str
    agency: str
    accountNumber: str
    balance: float
    accountType: str


class User(BaseModel):
    id: Optional[str | UUID]
    name: str
    email: EmailStr
    password: str
    account: List[BankAccount]


class Template(BaseModel):
    title: str
    name: str
    category: str
    fields: Json

    @model_validator(mode='before')
    def set_name(cls, values):
        title = values.get('title', '')
        name = title.lower().replace(" ", "_")
        values['name'] = name
        return values