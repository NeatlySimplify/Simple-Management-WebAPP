from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Scheduler(BaseModel):
    user: str
    nome: str
    status: bool
    inicio: datetime
    fim: datetime
    details: Optional[str]
    tag_tipo: str