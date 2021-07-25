import hashlib
from uuid import uuid4

from fastapi import APIRouter, Request
from loguru import logger

import src.core.actions as actions
import src.db.crud as crud
import src.db.tasks as tasks
from src.schemas import UserCreateBody

router = APIRouter()


@router.post("/token")
async def token(request: Request, userinfo: UserCreateBody):
    logger.info("POST request to endpoint /token from client {request.client.host}")
    token = str(uuid4())
    tokenhash = str(hashlib.sha256(bytes(token, encoding="utf8")).hexdigest())
    password = userinfo.password
    passhash = str(hashlib.sha256(bytes(password, encoding="utf8")).hexdigest())

    async with tasks.Database() as conn:
        await crud.new_user(
            conn, str(actions.gensnowflake()), tokenhash, userinfo.username, passhash
        )

    return {"token": token}
