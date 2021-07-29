from fastapi import APIRouter, Request
from loguru import logger

router = APIRouter()


@router.get("/servers")
async def servers_get(request: Request):
    logger.info(f"GET request to endpoint /servers from client {request.client.host}")


@router.post("/servers")
async def servers_post(request: Request):
    logger.info(f"POST request to endpoint /servers from client {request.client.host}")


@router.patch("/servers")
async def servers_patch(request: Request):
    logger.info(f"PATCH request to endpoint /servers from client {request.client.host}")


@router.delete("/servers")
async def servers_delete(request: Request):
    logger.info(
        f"DELETE request to endpoint /servers from client {request.client.host}"
    )
