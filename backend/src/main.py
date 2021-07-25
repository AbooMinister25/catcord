from fastapi import FastAPI, Request
from loguru import logger

from src.endpoints import messages, servers, token

app = FastAPI()

app.include_router(servers.router)
app.include_router(messages.router)
app.include_router(token.router)


@app.get("/")
async def home(request: Request):
    logger.info(f"GET request to endpoint / from client {request.client.host}")
    return {"message": "Welcome to Catcord!"}
