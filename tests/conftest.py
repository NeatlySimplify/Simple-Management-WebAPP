import hashlib
import os
from datetime import date
from random import choice, random, randrange

from faker import Faker
from pydantic import constr
import pytest

from app.Model import finance, people, scheduler, service, utils
from app.Routes import user

from app.Service import db_async_client

fake = Faker("pt_BR")  # noqa: F405


@pytest.fixture(scope="session")
def common_user_uuid():
    user = {
        "email": "ribeirodennis9@gmail.com",
        "senha": "24657122542"
    }
    db = db_async_client()
    
    yield user

#Data Instances

def gen_user () -> people.User:
    """
    docstring
    """
    return people.User(
        email=fake.free_email(),
        nome=fake.name(),
        sexo=random.choice("Masculino", "Feminino"),
        estado_civil=choice(list(utils.RelationshipTag)),
        details=fake.text(),
        tag_tipo=utils.PeopleTag.USER,
        nascimento=fake.date_between_dates(date(1924, 1, 1), date(2007, 1, 1))
)

def gen_client_pf() -> people.PessoaFisica:
    """
    docstring
    """
    user
