from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse
from loguru import logger
from starlette.exceptions import HTTPException as StarletteHttpException
from tortoise import Tortoise

import src.core.utils as utils
import src.database.crud.users as users_crud
from src.core.schemas import UserBody
from src.database.database import init_orm
from src.endpoints import messages, servers, users

app = FastAPI()

app.include_router(messages.router)
app.include_router(servers.router)
app.include_router(users.router)


@app.on_event("startup")
async def init_orm_startup():
    await init_orm()


@app.on_event("shutdown")
async def shutdown_orm():
    await Tortoise.close_connections()


@app.exception_handler(StarletteHttpException)
async def http_exception_handler(request: Request, exc):
    logger.exception(f"HTTP Exception {exc.status_code} on request URL {request.url}")
    exception = {"HTTP Exception": exc.detail, "Status Code": exc.status_code}
    return JSONResponse(exception, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_request_handler(request: Request, exc):
    logger.exception(f"Validation Error Occurred on request URL {request.url}")
    exception = {"Validation Error": exc.detail, "Status Code": exc.status_code}
    return JSONResponse(exception, status_code=400)


@app.get("/")
async def root(request: Request):
    logger.info(f"GET request to endpoint / from client {request.client.host}")


@app.post("/token")
async def token(request: Request, user_body: UserBody):
    logger.info(f"POST request to endpoint /token from client {request.client.host}")

    uid = user_body.uid
    password = user_body.password

    password_hash = utils.generate_sha256(password)

    authorized = await users_crud.auth_with_password(password_hash, uid)
    if not authorized:
        return HTTPException(status_code=403, detail="Invalid Credentials")

    user_token = str(uuid4())
    token_hash = utils.generate_sha256(user_token)
    await users_crud.update_user_token(password_hash, uid, token_hash)

    return {"token": user_token}
