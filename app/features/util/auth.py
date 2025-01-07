from http import HTTPStatus
from fastapi import HTTPException, Request
from datetime import datetime, timedelta
from decouple import config
import jwt
from starlette.middleware.base import BaseHTTPMiddleware
    

SECRET_KEY = config("secret")
ALGORITHM = config("algorithm")
TOKEN_EXPIRATION = float(config("jwtToken_expire_time"))
SESSION_SECRET_KEY = config("session_secret")
session_config = {
    "secret_key": SESSION_SECRET_KEY
}
tokens = {}


def extract_token(request: Request):
    # Extract the token from the cookie
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Access token is missing, redirecting to login.",
        )
    return token


def create_access_token(user_id: str):
    payload = {'sub': user_id}
    expiration_time = datetime.now() + timedelta(hours=TOKEN_EXPIRATION)
    payload['exp'] = datetime.timestamp(expiration_time)
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_token(token: str):
    try:
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        raise AssertionError("O Token Expirou")
    except jwt.DecodeError:
        raise RuntimeError("Não conseguiu decodar o token")
    except Exception as e:
        raise e

    
def verify(token: str):
    return tokens.get(token)

async def get_current_user(request: Request):
    try:
        token = extract_token(request)
        # Decode the JWT token
        if user_id := decode_token(token) is None:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="Invalid token payload.",
            )
        
        # # Fetch user info (validate the user)
        # user_exists = verify(token)
        # if not user_exists:
        #     raise HTTPException(
        #         status_code=HTTPStatus.UNAUTHORIZED,
        #         detail="User not found.",
        #     )
    except jwt.InvalidTokenError:
        # Raise an HTTPException for invalid token
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Invalid token.",
        )
    except ValueError as e:
        # Handle user validation errors
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail=str(e),
        )
    # Return the user object
    return user_id
