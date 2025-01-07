from contextlib import asynccontextmanager
import edgedb
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.templating import Jinja2Templates

cors_config = {
    "allow_origins": ["http://localhost:8000"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}

templates = Jinja2Templates(directory="./static/templates")


@asynccontextmanager
async def lifetime(app):
    app.state.edgedb = edgedb.create_async_client()
    await app.state.edgedb.ensure_connected()
    try:
        # Yield control to the application
        yield
    finally:
        # Shutdown: Close the EdgeDB client
        await app.state.edgedb.aclose()
        app.state.edgedb = None


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