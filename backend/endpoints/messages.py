import backend.db.tasks as tasks
import backend.db.crud as crud
import backend.core.actions as actions
from backend.schemas import NewMessageBody
import time
from fastapi import APIRouter, Header, Response

router = APIRouter()


@router.post("/new_message")
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


@router.get("/get_messages")
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
