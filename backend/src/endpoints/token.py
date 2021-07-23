import src.db.tasks as tasks
import src.db.crud as crud
import src.core.actions as actions
from src.core.logger import Logger
from src.schemas import UserCreateBody
from fastapi import APIRouter, Request
from uuid import uuid4
import hashlib

router = APIRouter()
logger = Logger(mode="file", filename="requests.log")


@router.post("/token")
async def token(request: Request, userinfo: UserCreateBody):
    await logger.log(
        "info", f"POST request to endpoint /token from client {request.client.host}"
    )
    token = str(uuid4())
    tokenhash = str(hashlib.sha256(bytes(token, encoding="utf8")).hexdigest())
    password = userinfo.password
    passhash = str(hashlib.sha256(bytes(password, encoding="utf8")).hexdigest())

    async with tasks.Database() as conn:
        await crud.new_user(
            conn, str(actions.gensnowflake()), tokenhash, userinfo.username, passhash
        )

    return {"token": token}
