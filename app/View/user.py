from . import *


router = APIRouter(
    prefix="/user",
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_user():
    return 0


@router.get("/{id}")
async def read_user(id: str):
    if id not in fake_users_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_users_db[id]["name"], "id": id}


@router.put("/{id}", responses={403: {"description": "Operation forbidden"}})
async def update_user(id: str):
    if id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the user: plumbus"
        )
    return {"id": id, "name": "The great Plumbus"}


@router.post("/{id}", responses={403: {"description": "Operation forbidden"}})
async def post_user(id: str):
    if id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the user: plumbus"
        )
    return {"id": id, "name": "The great Plumbus"}


@router.delete("/{id}", responses={403: {"description": "Operation forbidden"}})
async def delete_user(id: str):
    if id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the user: plumbus"
        )
    return {"id": id, "name": "The great Plumbus"}





