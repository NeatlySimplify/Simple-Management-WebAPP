from contextlib import asynccontextmanager
import functools
from http import HTTPStatus
import edgedb
from fastapi import HTTPException, Request
from edgedb import errors


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
    

def handle_database_errors(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        
        except errors.QueryError as e:
            return HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail={
                    "status": "error",
                    "message": "Query error occurred.",
                    "details": str(e)
                }
            )
        
        except errors.IntegrityError as e:
            return HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail={
                    "status": "error",
                    "message": "Integrity constraint violated.",
                    "details": str(e)
                }
            )

        except errors.ExecutionError as e:
            return HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail={
                    "status": "error",
                    "message": "Execution error occurred during query execution.",
                    "details": str(e)
                }
            )
        
        except errors.ProtocolError as e:
            return HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail={
                    "status": "error",
                    "message": "Protocol communication error.",
                    "details": str(e)
                }
            )

        except errors.AccessError as e:
            return HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail={
                    "status": "error",
                    "message": "Access denied.",
                    "details": str(e)
                }
            )

        except errors.BackendError as e:
            return HTTPException(
                status_code=HTTPStatus.SERVICE_UNAVAILABLE,
                detail={
                    "status": "error",
                    "message": "Database backend error.",
                    "details": str(e)
                }
            )

        except errors.AvailabilityError as e:
            return HTTPException(
                status_code=HTTPStatus.SERVICE_UNAVAILABLE,
                detail={
                    "status": "error",
                    "message": "Database is temporarily unavailable.",
                    "details": str(e)
                }
            )
        
        except errors.QueryTimeoutError as e:
            return HTTPException(
                status_code=HTTPStatus.REQUEST_TIMEOUT,
                detail={
                    "status": "error",
                    "message": "The query execution timed out.",
                    "details": str(e)
                }
            )
        
        except Exception as e:
            return HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail={
                    "status": "error",
                    "message": "An unexpected error occurred.",
                    "details": str(e)
                }
            )
    return wrapper