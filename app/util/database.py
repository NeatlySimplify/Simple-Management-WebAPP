from contextlib import asynccontextmanager
import edgedb
from fastapi import Request


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

def get_edgedb_client(request: Request) -> edgedb.AsyncIOClient:
    return request.app.state.edgedb
    
## Decorator to handle common database errors with the same patterns
## Still don't know how to use it, will try again later

# def handle_database_errors(func):
#     @functools.wraps(func)
#     async def wrapper(*args, **kwargs):
#         try:
#             return await func(*args, **kwargs)
#         except (errors.InternalServerError, errors.AvailabilityError, errors.BackendError) as e:
#             # Return the JSONResponse directly instead of raising it
#             return JSONResponse(
#                 status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
#                 content={
#                     "status": "error",
#                     "message": "Database error occurred.",
#                     "details": str(e)
#                 }
#             )
#         except errors.ExecutionError as e:
#             return JSONResponse(
#                 status_code=HTTPStatus.BAD_REQUEST,
#                 content={
#                     "status": "error",
#                     "message": "Invalid execution.",
#                     "details": str(e)
#                 }
#             )
#         except Exception as e:
#             # Catch any other unforeseen errors
#             return JSONResponse(
#                 status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
#                 content={
#                     "status": "error",
#                     "message": "An unexpected error occurred.",
#                     "details": str(e)
#                 }
#             )
#     return wrapper