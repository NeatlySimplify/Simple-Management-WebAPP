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


def create_access_token(user_id: str):
    expiration = datetime.now(timezone.utc) + timedelta(hours=TOKEN_EXPIRATION)
    payload = {
        "sub": user_id,
        "exp": expiration,  # datetime object, jwt will convert it to a Unix timestamp
        "iat": datetime.now(timezone.utc),  # datetime object, jwt will convert it to a Unix timestamp
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_token(token: str):
    try:
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        print("Error: Token has expired")
    except jwt.DecodeError:
        print("Error: Invalid token")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

    
def verify(token: str):
    return tokens.get(token)

async def get_current_user(request: Request):
    try:
        # Extract the token from the cookie
        token = request.cookies.get("access_token")
        if not token:
            return RedirectResponse(url="/login")
        
        # Decode the JWT token
        user = decode_token(token)
        if user is None:
            raise ValueError("Missing user id in token payload")
        
        # Fetch user info (validate the user)
        user_exists = verify(token)
        if not user_exists:
            raise ValueError("User not found")
        
    except jwt.InvalidTokenError:
        # Redirect to login page if token is invalid
        return RedirectResponse(url="/login")
    except ValueError as e:
        # Handle user validation errors
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail=str(e),
        )
    # Return the user object
    return {'id': user}

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
    # Compare the password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

