from decouple import config
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext






## For development purposes the tokens dict will save jwt token as keys
## on production a memcached container will be used
