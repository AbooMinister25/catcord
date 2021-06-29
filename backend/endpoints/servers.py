import backend.db.tasks as tasks
import backend.db.crud as crud
import backend.core.actions as actions
from backend.schemas import NewServerBody
from fastapi import APIRouter, Header, Response
import hashlib

router = APIRouter()


@router.post("/new_server")
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