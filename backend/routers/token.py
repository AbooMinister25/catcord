import backend.db.tasks as tasks
import backend.db.crud as crud
import backend.core.actions as actions
from backend.schemas import UserCreateBody
from fastapi import APIRouter, Header, Response
from uuid import uuid4
import hashlib

router = APIRouter()


@router.post("/token")
async def token(userinfo: UserCreateBody):
    token = str(uuid4())
    tokenhash = str(hashlib.sha256(bytes(token, encoding="utf8")).hexdigest())
    password = userinfo.password
    passhash = str(hashlib.sha256(bytes(password, encoding="utf8")).hexdigest())

    async with tasks.Database() as conn:
        await crud.new_user(
            conn, str(actions.gensnowflake()), tokenhash, userinfo.username, passhash
        )

    return {"token": token}
