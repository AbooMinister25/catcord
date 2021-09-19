from fastapi import APIRouter, Request
from loguru import logger

from src.core.ratelimits import Ratelimiter

router = APIRouter()

limiter = Ratelimiter(1, 60, 20)


@router.get("/messages")
@limiter.limit()
async def messages_get(request: Request):
    logger.info(f"GET request to endpoint /messages from client {request.client.host}")


@router.post("/messages")
async def messages_post(request: Request):
    logger.info(f"POST request to endpoint /messages from client {request.client.host}")


@router.patch("/messages")
async def messages_patch(request: Request):
    logger.info(
        f"PATCH request to endpoint /messages from client {request.client.host}"
    )


@router.delete("/messages")
async def messages_delete(request: Request):
    logger.info(
        f"DELETE request to endpoint /messages from client {request.client.host}"
    )
