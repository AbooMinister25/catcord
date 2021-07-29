from uuid import uuid4

from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from loguru import logger
from starlette.responses import JSONResponse

import src.core.utils as utils
import src.database.crud.users as users
from src.core.schemas import UserCreateBody

router = APIRouter()


@router.get("/users")
async def users_get(request: Request, user_id: str):
    logger.info(f"GET request to endpoint /users from client {request.client.host}")

    username = await users.get_user_info(user_id)

    if not username:
        return HTTPException(status_code=403, detail="UID does not exist")

    content = {"username": username}

    return JSONResponse(content=content)


@router.post("/users")
async def users_post(request: Request, new_user_info: UserCreateBody):
    logger.info(f"POST request to endpoint /users from client {request.client.host}")

    username = new_user_info.username
    password = new_user_info.password
    email = new_user_info.email

    if await users.check_email_exists(email):
        return HTTPException(detail="Email already exists", status_code=400)

    uid = str(utils.gensnowflake())
    token = str(uuid4())

    password_hash = utils.generate_sha256(password)
    token_hash = utils.generate_sha256(token)

    await users.create_user(username, password_hash, email, uid, token_hash)

    content = {"uid": uid, "token": token}
    return JSONResponse(content=content)


@router.patch("/users")
async def users_patch(request: Request):
    logger.info(f"PATCH request to endpoint /users from client {request.client.host}")


@router.delete("/users")
async def users_delete(request: Request):
    logger.info(f"DELETE request to endpoint /users from client {request.client.host}")


@router.get("/users/me")
async def users_me(request: Request):
    logger.info(f"POST request to endpoint /users/me from client {request.client.host}")
