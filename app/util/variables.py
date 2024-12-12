from decouple import config
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext


SECRET_KEY = config("secret")
ALGORITHM = config("algorithm")
TOKEN_EXPIRATION = float(config("jwtToken_expire_time"))
SESSION_SECRET_KEY = config("session_secret")
cors_config = {
    "allow_origins": ["http://localhost:8000"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
session_config = {
    "secret_key": SESSION_SECRET_KEY
}
templates = Jinja2Templates(directory="./app/static/templates")

## For development purposes the tokens dict will save jwt token as keys
## on production a memcached container will be used
tokens = {}