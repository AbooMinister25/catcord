import asyncpg
from loguru import logger


async def new_user(
    connection: asyncpg.Connection,
    user_id: str,
    tokenhash: str,
    username: str,
    passhash: str,
):
    logger.info("Attempting to add a new user to DB")
    try:
        await connection.execute(
            f"INSERT INTO USERS VALUES({user_id}, '{tokenhash}', '{username}', '{passhash}');"
        )

        logger.success("Successfully added a new user to database")
    except Exception:
        logger.error("Exception occured while trying to add a user to database")


async def new_server(
    connection: asyncpg.Connection, server_id: str, owner_id: str, server_name: str
):
    logger.info("Attempting to add a server to database")
    try:
        await connection.execute(
            f"INSERT INTO SERVERS VALUES('{server_id}', '{owner_id}', '{server_name}');"
        )
        logger.success("Successfully added a server to database")
    except Exception:
        logger.error("Exception occured while trying to add a server to database")


async def new_message(
    connection: asyncpg.Connection,
    message_id: str,
    timesent: int,
    sender_id: str,
    server_id: str,
    message_content: str,
):
    logger.info("Attempting to add a new message to database")
    try:
        await connection.execute(
            f"INSERT INTO MESSAGES VALUES('{message_id}', \
            '{timesent}', '{sender_id}', '{server_id}', '{message_content}');"
        )
        logger.success("Successfully added a new message to database")
    except Exception:
        logger.error("Exception occured while trying to add a message to database")


async def get_messages(connection: asyncpg.Connection, server_id: str):
    logger.info("Attempting to get messages from database")
    try:
        messages = await connection.fetch(
            f"SELECT * FROM MESSAGES WHERE server_id='{server_id}'"
        )
        logger.success("Successfully retrieved messages from database")
        return messages
    except Exception:
        logger.error("Exception occured while fetching messages from database")
