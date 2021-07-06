import asyncpg
from backend.core.logger import Logger

logger = Logger(mode="file", filename="database.log")


async def new_user(
    connection: asyncpg.Connection,
    user_id: str,
    tokenhash: str,
    username: str,
    passhash: str,
):
    await logger.info("Attempting to add a new user to DB")
    try:
        await connection.execute(
            f"INSERT INTO USERS VALUES({user_id}, '{tokenhash}', '{username}', '{passhash}');"
        )
        await logger.success("Successfully added a new user to DB")
    except:
        await logger.error(
            "Exception occured while trying to add a user to database", exc=True
        )


async def new_server(
    connection: asyncpg.Connection, server_id: str, owner_id: str, server_name: str
):
    await logger.info("Attempting to add a server to DB")
    try:
        await connection.execute(
            f"INSERT INTO SERVERS VALUES('{server_id}', '{owner_id}', '{server_name}');"
        )
        await logger.success("Successfully added a server to DB")
    except:
        await logger.error(
            "Exception occured while trying to add a server to database", exc=True
        )


async def new_message(
    connection: asyncpg.Connection,
    message_id: str,
    timesent: int,
    sender_id: str,
    server_id: str,
    message_content: str,
):
    await logger.info("Attempting to add a new message to DB")
    try:
        await connection.execute(
            f"INSERT INTO MESSAGES VALUES('{message_id}', \
            '{timesent}', '{sender_id}', '{server_id}', '{message_content}');"
        )
        await logger.success("Successfully added a new message to DB")
    except:
        await logger.error(
            "Exception occured while trying to add a message to database", exc=True
        )


async def get_messages(connection: asyncpg.Connection, server_id: str):
    await logger.info("Attempting to get messages from DB")
    try:
        messages = await connection.fetch(
            f"SELECT * FROM MESSAGES WHERE server_id='{server_id}'"
        )
        await logger.success("Successfully retrieved messages from DB")
        return messages
    except:
        await logger.error(
            "Exception occured while fetching messages from DB", exc=True
        )
