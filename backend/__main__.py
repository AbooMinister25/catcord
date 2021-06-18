import backend.db.tasks as tasks
import backend.db.crud as crud
import backend.core.actions as actions
import hashlib
from uuid import uuid4
from fastapi import FastAPI, Header, Response
from pydantic import BaseModel
import time

app = FastAPI()


class UserCreateBody(BaseModel):
    username: str
    password: str


class NewServerBody(BaseModel):
    name: str


class NewMessageBody(BaseModel):
    server_id: str
    message_content: str


@app.get("/")
async def home():
    return {"message": "Send a POST request to /token to generate a token."}


@app.post("/token")
async def token(userinfo: UserCreateBody):
    token = str(uuid4())
    tokenhash = str(hashlib.sha256(bytes(token, encoding="utf8")).hexdigest())
    password = userinfo.password
    passhash = str(hashlib.sha256(bytes(password, encoding="utf8")).hexdigest())

    async with tasks.Database() as conn:
        await crud.new_user(
            conn, str(actions.gensnowflake()), tokenhash, userinfo.username, passhash
        )

    return {"token": token}


@app.post("/new_server")
async def new_server(
    response: Response, serverinfo: NewServerBody, Auth: str = Header(None)
):
    if Auth is None:
        response.status_code = 403
        return {"error": "No token supplied. Please submit a token."}
    tokenhash = hashlib.sha256(bytes(Auth, encoding="utf8")).hexdigest()

    async with tasks.Database() as conn:
        userdata = await conn.fetchrow(
            f"SELECT * FROM USERS WHERE TOKEN='{tokenhash}';"
        )
        if userdata is None:
            response.status_code = 403
            return {
                "error": "Token supplied is invalid. \
                Please correct your token or get one by sending a post request to /token ."
            }
        serverid = str(actions.gensnowflake())
        await crud.new_server(conn, serverid, userdata[0], serverinfo.name)
    return {"server_id": serverid}


@app.post("/new_message")
async def new_message(
    response: Response, messageinfo: NewMessageBody, Auth: str = Header(None)
):
    if Auth is None:
        response.status_code = 403
        return {"error": "No token supplied. Please submit a token."}
    tokenhash = actions.gentokenhash(Auth)

    async with tasks.Database() as conn:
        userdata = await conn.fetchrow(
            f"SELECT * FROM USERS WHERE TOKEN='{tokenhash}';"
        )

        if userdata is None:
            response.status_code = 403
            return {
                "error": "Token supplied is invalid. \
                Please correct your token or get one by sending a post request to /token ."
            }
        messageid = str(actions.gensnowflake())

        await crud.new_message(
            conn,
            messageid,
            time.time_ns(),
            userdata[0],
            messageinfo.server_id,
            messageinfo.message_content,
        )

    return {"message_id": messageid}


@app.get("/get_messages")
async def get_messages(
    response: Response, server_id: str = None, Auth: str = Header(None)
):
    if Auth is None:
        return {"error": "No token supplied. Please submit a token."}

    async with tasks.Database() as conn:
        tokenhash = actions.gentokenhash(Auth)
        userdata = await conn.fetchrow(f"SELECT * FROM USERS WHERE TOKEN='{tokenhash}'")
        if userdata is None:
            return {
                "error": "Token supplied is invalid. \
                    Please correct your token or get one by sending a post request to /tokens ."
            }

        messages = await crud.get_messages(conn, server_id)
        messagelist = []

        for element in messages:
            message = {}
            message["id"] = element[0]
            message["timestamp"] = element[1]
            message["sender"] = element[2]
            sender_name = await conn.fetchrow(
                f"SELECT USERNAME FROM USERS WHERE ID='{element[2]}'"
            )
            message["sender_name"] = sender_name["username"]
            message["content"] = element[4]
            messagelist.append(message)

    return messagelist
