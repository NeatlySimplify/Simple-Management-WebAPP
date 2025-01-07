from fastapi import Request, HTTPException
from http import HTTPStatus
from ..util.auth import verify, decode_token

def redirect_if_authenticated(request: Request):
    token = request.cookies.get("access_token")
    try:
        decoded = decode_token(token)  # Your custom JWT decoding logic
        authenticated = verify(decoded)  # Your custom verification logic
        if authenticated:
            raise HTTPException(
                status_code=HTTPStatus.TEMPORARY_REDIRECT,
                detail="Authenticated",
                headers={"Location": "/"}  # Redirect to home if authenticated
            )
    except Exception:
        pass  # If any exception occurs, treat the user as not authenticated