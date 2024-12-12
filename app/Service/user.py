from unittest import result
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials
from app.util import get_edgedb_client
from edgedb import errors
from http import HTTPStatus

    
async def logout(request, user_id):
    from app.queries.logout_async_edgeql import logout
    db_client = get_edgedb_client(request)
    try:
        await logout(db_client, user_id)
        return JSONResponse(
            status_code=HTTPStatus.OK,
            content={
                "status": "success",
                "message": "User was Updated Successfully"
            }
        )
    except (errors.InternalServerError, errors.AvailabilityError, errors.BackendError) as e:
        # Return the JSONResponse directly instead of raising it
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={
                "status": "error",
                "message": "Database error occurred.",
                "details": str(e)
            }
        )
    except errors.ExecutionError as e:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={
                "status": "error",
                "message": "Invalid execution.",
                "details": str(e)
            }
        )
    except Exception as e:
        # Catch any other unforeseen errors
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={
                "status": "error",
                "message": "An unexpected error occurred.",
                "details": str(e)
            }
        )


async def change_password(request: Request, new_password):
    from app.queries.update_user_async_edgeql import update_user
    from app.util import hash_password
    db_client = get_edgedb_client(request)
    hashed_pw = hash_password(new_password)
    try:
        await update_user(
            executor=db_client,
                password=hashed_pw
        )
        return JSONResponse(
            status_code=HTTPStatus.OK,
            content={
                "status": "success",
                "message": "User was Updated Successfully"
            }
        )
    except (errors.InternalServerError, errors.AvailabilityError, errors.BackendError) as e:
        # Return the JSONResponse directly instead of raising it
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={
                "status": "error",
                "message": "Database error occurred.",
                "details": str(e)
            }
        )
    except errors.ExecutionError as e:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={
                "status": "error",
                "message": "Invalid execution.",
                "details": str(e)
            }
        )
    except Exception as e:
        # Catch any other unforeseen errors
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={
                "status": "error",
                "message": "An unexpected error occurred.",
                "details": str(e)
            }
        )


async def update_user():
    pass

async def create_template():
    pass

async def update_template():
    pass

async def delete_template():
    pass

async def get_template():
    pass

async def get_all_templates():
    pass

async def create_bank_account():
    pass

async def update_bank_account():
    pass

async def get_bank_account():
    pass

async def get_all_bank_accounts():
    pass

async def get_balance():
    pass