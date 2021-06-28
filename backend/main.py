from fastapi import FastAPI
from backend.routers import servers, messages, token

app = FastAPI()

app.include_router(servers.router)
app.include_router(messages.router)
app.include_router(token.router)


@app.get("/")
async def home():
    return {"message": "Send a POST request to /token to generate a token."}
