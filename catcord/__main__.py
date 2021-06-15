import hashlib
from uuid import uuid4

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Send a POST request to /token to generate a token."}

@app.post("/token")
async def token():
    token = str(uuid4())
    tokenhash = hashlib.sha256(bytes(token)).hexdigest()
