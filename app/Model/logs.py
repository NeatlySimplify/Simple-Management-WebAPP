from pydantic import BaseModel, Json


class Auditable(BaseModel):
    user: str
    action: str
    details: Json
