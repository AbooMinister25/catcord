from uuid import uuid4

from fastapi import APIRouter, Depends, Request
from fastapi.exceptions import HTTPException
from loguru import logger
from starlette.responses import JSONResponse

import src.core.utils as utils
from src.core.schemas import UserCreateBody
from src.database.crud.users import UserDAL, get_user_dal

router = APIRouter()


@router.get("/users")
async def users_get(
    request: Request, user_id: str, user_dal: UserDAL = Depends(get_user_dal)
):
    logger.info(f"GET request to endpoint /users from client {request.client.host}")

    username = await user_dal.get_public_user_info(user_id)

    if not username:
        return HTTPException(status_code=403, detail="UID does not exist")

    content = {"username": username}

    return JSONResponse(content=content)


@router.post("/users")
async def users_post(
    request: Request,
    new_user_info: UserCreateBody,
    user_dal: UserDAL = Depends(get_user_dal),
):
    logger.info(f"POST request to endpoint /users from client {request.client.host}")

    username = new_user_info.username
    password = new_user_info.password
    email = new_user_info.email

    if await user_dal.check_email_exists(email):
        return HTTPException(detail="Email already exists", status_code=400)

    uid = str(utils.gensnowflake())
    token = str(uuid4())

    password_hash = utils.generate_sha256(password)
    token_hash = utils.generate_sha256(token)

    await user_dal.create_user(username, password_hash, email, uid, token_hash)

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
