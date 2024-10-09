from . import *


class Finance(BaseModel):
    user: str
    nome: str
    valor: float
    efetivado: bool
    tag_tipo: str
    categoria: str
    details: str = ''
    subcategoria: str
