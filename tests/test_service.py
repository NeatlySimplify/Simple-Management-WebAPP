from . import *
import json


class Service:
    id_Service: str = fake.random_number(digits=None, fix_len=18)
    status: str = choice(True, False)
    valor: float = random()
    categoria: str = "Process"
    details: str = fake.text()
    custom: json = json.dump({
        "Comarca": fake.building_name,
        "Fase": choice("Concluído", "Em Andamento", "Não iniciado"),
        "rito": choice("Comum", "Sumaríssimo"),
        "forum": fake.city_name(),
        "vara": choice("Penal", "Familiar", "Consumidor")
    })