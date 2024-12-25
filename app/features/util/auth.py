from multiprocessing import Value
import bcrypt
from http import HTTPStatus
from fastapi.responses import RedirectResponse
from fastapi import HTTPException, Request
from datetime import datetime, timedelta, timezone
from .variables import (
    SECRET_KEY,
    ALGORITHM,
    TOKEN_EXPIRATION,
    tokens
)
import jwt
from starlette.middleware.base import BaseHTTPMiddleware


class CookieInitializationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        # Initialize the `access_token` cookie if missing
        if not request.cookies.get("access_token"):
            response.set_cookie(
                key="access_token",
                value="",  # Default empty value
                httponly=False,
                secure=False,
                samesite="lax"
            )
        return response


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

def hash_password(password: str) -> str:
    if not isinstance(password, str):
        raise ValueError("Password must be a string.")
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Return the hashed password as a string
    return hashed_password.decode('utf-8')


def verify_password(password: str, hashed_password: str) -> bool:
    if not isinstance(password, str) or not isinstance(hashed_password, str):
        raise ValueError("Both password and hashed_password must be strings.")
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

