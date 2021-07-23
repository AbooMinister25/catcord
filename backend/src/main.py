from fastapi import FastAPI, Request
from src.endpoints import servers, messages, token
from src.core.logger import Logger

app = FastAPI()
logger = Logger(mode="file", filename="requests.log")

app.include_router(servers.router)
app.include_router(messages.router)
app.include_router(token.router)


@app.get("/")
async def home(request: Request):
    await logger.log(
        "info", f"GET request to endpoint / from client {request.client.host}"
    )
    return {"message": "Send a POST request to /token to generate a token."}
